import pytest
import stim
from surface_code import generate_circuit


gen_test_params = [
    ("surface_code:unrotated_memory_x", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 2, 2, 0, 0, 0, 0),
    ("surface_code:unrotated_memory_z", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 2, 2, 0, 0, 0, 0),
    ("surface_code:rotated_memory_x", 3, 2, 0.001, 0.002, 0.003, 0.004),
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
        after_reset_flip_probability=after_reset_flip_probability
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
