# Copyright 2022 Oscar Higgott

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#      http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import stim
from stimcircuits.surface_code import generate_circuit
from typing import Set

gen_test_params_surface_code = [
    ("surface_code:unrotated_memory_x", 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 2, 2, 0, 0.01, 0, 0),
    ("surface_code:unrotated_memory_z", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 2, 2, 0, 0.01, 0, 0),
    ("surface_code:rotated_memory_x", 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 2, 2, 0, 0.01, 0, 0),
    ("surface_code:rotated_memory_z", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 2, 2, 0, 0.01, 0, 0)
]
gen_test_params_distances_surface_code = [
    ("surface_code:unrotated_memory_x", 3, 3, 3, 10, 0.001, 0.002, 0.003,
     0.004),
    ("surface_code:unrotated_memory_x", 5, 3, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 2, 2, 2, 2, 0, 0.01, 0, 0),
    ("surface_code:unrotated_memory_z", 3, 5, 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 5, 5, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 2, 2, 2, 2, 0, 0.01, 0, 0),
    ("surface_code:rotated_memory_x", 3, 5, 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 5, 3, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 2, 2, 2, 2, 0, 0.01, 0, 0),
    ("surface_code:rotated_memory_z", 3, 5, 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 5, 3, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 2, 2, 2, 2, 0, 0.01, 0, 0)
]

gen_test_params_rectangular_rotated_surface_code = [
    ("surface_code:rotated_memory_x", 3, 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 5, 3, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 3, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_x", 2, 3, 2, 0, 0.01, 0, 0),
    ("surface_code:rotated_memory_z", 3, 5, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 5, 3, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:rotated_memory_z", 2, 2, 2, 0, 0.01, 0, 0)
]

gen_test_params_rectangular_unrotated_surface_code = [
    ("surface_code:unrotated_memory_x", 3, 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 5, 3, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 3, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_x", 2, 3, 2, 0, 0.01, 0, 0),
    ("surface_code:unrotated_memory_z", 3, 5, 2, 0.001, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 5, 3, 1, 0.1, 0.002, 0.003, 0.004),
    ("surface_code:unrotated_memory_z", 2, 2, 2, 0, 0.01, 0, 0)
]


@pytest.mark.parametrize(
    "code_task,distance,rounds,after_clifford_depolarization,before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_surface_code
)
def test_generate_circuit(
        code_task: str,
        distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
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


gen_test_params_toric_code = [
    ("toric_code:unrotated_memory_x", 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_x", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_x", 2, 2, 0, 0.01, 0, 0),
    ("toric_code:unrotated_memory_z", 3, 2, 0.001, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_z", 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_z", 2, 2, 0, 0.01, 0, 0),
]

gen_test_params_rectangular_toric_code = [
    ("toric_code:unrotated_memory_x", 3, 3, 10, 0.001, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_x", 5, 3, 1, 0.1, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_x", 3, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_x", 2, 2, 2, 0, 0.01, 0, 0),
    ("toric_code:unrotated_memory_z", 3, 2, 2, 0.001, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_z", 2, 5, 1, 0.1, 0.002, 0.003, 0.004),
    ("toric_code:unrotated_memory_z", 2, 2, 2, 0, 0.01, 0, 0),
]


@pytest.mark.parametrize(
    "code_task,distance,rounds,after_clifford_depolarization,before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_surface_code + gen_test_params_toric_code
)
def test_generated_circuit_graphlike_distance(
        code_task: str,
        distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
    for b in (False, True):
        circuit = generate_circuit(
            code_task=code_task,
            distance=distance,
            rounds=rounds,
            after_clifford_depolarization=after_clifford_depolarization,
            before_round_data_depolarization=before_round_data_depolarization,
            before_measure_flip_probability=before_measure_flip_probability,
            after_reset_flip_probability=after_reset_flip_probability,
            exclude_other_basis_detectors=b
        )
        dem = circuit.detector_error_model(decompose_errors=True)
        shortest_error = dem.shortest_graphlike_error()
        assert len(shortest_error) == distance


@pytest.mark.parametrize(
    "code_task,distance,x_distance,z_distance,rounds,after_clifford_depolarization,"
    "before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_distances_surface_code
)
def test_generated_circuit_with_distances_graphlike_distance(
        code_task: str,
        distance: int,
        x_distance: int,
        z_distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
    for b in (False, True):
        circuit = generate_circuit(
            code_task=code_task,
            distance=distance,
            x_distance=x_distance,
            z_distance=z_distance,
            rounds=rounds,
            after_clifford_depolarization=after_clifford_depolarization,
            before_round_data_depolarization=before_round_data_depolarization,
            before_measure_flip_probability=before_measure_flip_probability,
            after_reset_flip_probability=after_reset_flip_probability,
            exclude_other_basis_detectors=b
        )
        dem = circuit.detector_error_model(decompose_errors=True)
        shortest_error = dem.shortest_graphlike_error()
        assert len(shortest_error) == distance


@pytest.mark.parametrize(
    "code_task,x_distance,z_distance,rounds,after_clifford_depolarization,"
    "before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_rectangular_rotated_surface_code
)
def test_generated_rectangular_circuit_graphlike_distance(
        code_task: str,
        x_distance: int,
        z_distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
    for b in (False, True):
        circuit = generate_circuit(
            code_task=code_task,
            x_distance=x_distance,
            z_distance=z_distance,
            rounds=rounds,
            after_clifford_depolarization=after_clifford_depolarization,
            before_round_data_depolarization=before_round_data_depolarization,
            before_measure_flip_probability=before_measure_flip_probability,
            after_reset_flip_probability=after_reset_flip_probability,
            exclude_other_basis_detectors=b
        )
        dem = circuit.detector_error_model(decompose_errors=True)
        shortest_error = dem.shortest_graphlike_error()
        assert len(shortest_error) == z_distance if code_task[-1] == 'x' else \
            x_distance


@pytest.mark.parametrize(
    "code_task,x_distance,z_distance,rounds,after_clifford_depolarization,"
    "before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_rectangular_unrotated_surface_code + gen_test_params_rectangular_toric_code
)
def test_not_implemented_rectangular_circuit(
        code_task: str,
        x_distance: int,
        z_distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
    with pytest.raises(NotImplementedError) as e_info:
        for b in (False, True):
            circuit = generate_circuit(
                code_task=code_task,
                x_distance=x_distance,
                z_distance=z_distance,
                rounds=rounds,
                after_clifford_depolarization=after_clifford_depolarization,
                before_round_data_depolarization=before_round_data_depolarization,
                before_measure_flip_probability=before_measure_flip_probability,
                after_reset_flip_probability=after_reset_flip_probability,
                exclude_other_basis_detectors=b
            )


@pytest.mark.parametrize(
    "code_task,distance,rounds,after_clifford_depolarization,before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_surface_code + gen_test_params_toric_code
)
def test_no_hyperedges_when_exclude_other_basis_detectors(
        code_task: str,
        distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
    circuit = generate_circuit(
        code_task=code_task,
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=after_clifford_depolarization,
        before_round_data_depolarization=before_round_data_depolarization,
        before_measure_flip_probability=before_measure_flip_probability,
        after_reset_flip_probability=after_reset_flip_probability,
        exclude_other_basis_detectors=True
    )
    dem = circuit.detector_error_model(decompose_errors=False)
    # The following line will raise an exception if hyperedges are present
    dem.shortest_graphlike_error(ignore_ungraphlike_errors=False)


@pytest.mark.parametrize(
    "code_task,distance,rounds,after_clifford_depolarization,before_round_data_depolarization,"
    "before_measure_flip_probability,after_reset_flip_probability",
    gen_test_params_toric_code
)
def test_no_boundary_for_toric_code_circuits(
        code_task: str,
        distance: int,
        rounds: int,
        after_clifford_depolarization: float,
        before_round_data_depolarization: float,
        before_measure_flip_probability: float,
        after_reset_flip_probability: float
) -> None:
    circuit = generate_circuit(
        code_task=code_task,
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=after_clifford_depolarization,
        before_round_data_depolarization=before_round_data_depolarization,
        before_measure_flip_probability=before_measure_flip_probability,
        after_reset_flip_probability=after_reset_flip_probability,
        exclude_other_basis_detectors=True
    )
    dem = circuit.detector_error_model(decompose_errors=False)
    for instruction in dem:
        if isinstance(instruction, stim.DemInstruction) and instruction.type == "error":
            num_dets = sum(1 for t in instruction.targets_copy() if t.is_relative_detector_id())
            assert num_dets > 1
