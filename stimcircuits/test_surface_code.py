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
