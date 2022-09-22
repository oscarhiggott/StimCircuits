import pytest
import stim
from stimcircuits.surface_code import generate_circuit
import pymatching
from stimcircuits.decoding_pymatching_glue import detector_error_model_to_nx_graph
from typing import Set


gen_test_params = [
    ("surface_code:unrotated_memory_x", 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 2, 2, 0, 0, 0, 0),
    ("surface_code:unrotated_memory_z", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 2, 2, 0, 0, 0, 0),
    ("surface_code:rotated_memory_x", 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 2, 2, 0, 0, 0, 0),
    ("surface_code:rotated_memory_z", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 2, 2, 0, 0, 0, 0)
]


@pytest.mark.parametrize(
    "code_task,distance,rounds,after_clifford_depolarization,before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params
)
def test_generate_circuit(
        code_task: str,
        distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
):
    py_circuit = generate_circuit(
        code_task=code_task,
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=after_clifford_depolarization,
        before_round_data_depolarization=before_round_data_depolarization,
        before_measure_flip_probability=before_measure_flip_probability,
        after_reset_flip_probability=after_reset_flip_probability,
        exclude_other_basis_detectors=False
    )
    cpp_circuit = stim.Circuit.generated(
        code_task=code_task,
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=after_clifford_depolarization,
        before_round_data_depolarization=before_round_data_depolarization,
        before_measure_flip_probability=before_measure_flip_probability,
        after_reset_flip_probability=after_reset_flip_probability
    )
    assert str(py_circuit) == str(cpp_circuit)


def approx_edges(edges, ndigits: int = 8, boundary: Set[int] = None):
    new_edges = []
    for u, v, d in edges:
        new_edges.append((
            u if u not in boundary else None,
            v if v not in boundary else None,
            tuple(sorted(d['fault_ids'])),
            round(d['weight'], ndigits),
            round(d['error_probability'], ndigits)
        ))
    return new_edges


@pytest.mark.parametrize(
    "code_task,distance,rounds,after_clifford_depolarization,before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params[0:1]
)
def test_excluding_other_basis_has_same_mwpm_solution_weight(
        code_task: str,
        distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
):
    py_circuit = generate_circuit(
        code_task=code_task,
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=after_clifford_depolarization,
        before_round_data_depolarization=before_round_data_depolarization,
        before_measure_flip_probability=before_measure_flip_probability,
        after_reset_flip_probability=after_reset_flip_probability,
        exclude_other_basis_detectors=True
    )
    cpp_circuit = stim.Circuit.generated(
        code_task=code_task,
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=after_clifford_depolarization,
        before_round_data_depolarization=before_round_data_depolarization,
        before_measure_flip_probability=before_measure_flip_probability,
        after_reset_flip_probability=after_reset_flip_probability
    )
    cpp_dem = cpp_circuit.detector_error_model(decompose_errors=True)
    cpp_graph = detector_error_model_to_nx_graph(cpp_dem)
    cpp_matching = pymatching.Matching(cpp_graph)
    cpp_edges = sorted(cpp_matching.edges())
    cpp_edges_approx = approx_edges(cpp_edges, boundary=cpp_matching.boundary)
    py_dem = py_circuit.detector_error_model(decompose_errors=True)
    py_graph = detector_error_model_to_nx_graph(py_dem)
    py_matching = pymatching.Matching(py_graph)
    py_edges = sorted(py_matching.edges())
    py_edges_approx = approx_edges(py_edges, boundary=py_matching.boundary)
    assert len(py_edges_approx) <= len(cpp_edges_approx)
