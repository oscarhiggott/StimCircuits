## StimCircuits

This package is essentially a translation (from C++ to Python) of some of the code for generating example circuits 
included in [Stim](https://github.com/quantumlib/Stim). It currently only supports surface code circuits, so is 
essentially a translation of [this Stim file](https://github.com/quantumlib/Stim/blob/cbc9caf2a77d5c2b96cd82170b42ef59637baf9c/src/stim/gen/gen_surface_code.cc#L349), 
but with a few additional features. 
This Python implementation is useful for making modifications to the example circuits, without needing to use the Stim 
C++ API.

To install the package, run `pip install -e .` in the root directory. The `stimcircuits.generate_circuit` method can 
then be used to generate circuits, and takes the same arguments as the [`stim.Circuit.generated`](https://github.com/quantumlib/Stim/blob/main/doc/python_api_reference_vDev.md#stim.Circuit.generated) 
method (but currently only supports surface code circuits). `stimcircuits.generate_circuit` also includes the 
additional argument `exclude_other_basis_detectors` which, if set to `True`, removes the detectors in the opposite 
basis to that of the measured logical observable. This can be useful for running simulations with decoders (such as 
minimum-weight perfect matching and union-find) that ignore hyperedge fault mechanisms in the detector error model, 
as the detectors in the opposite basis are not relevant to the decoding problem, but increase the size of the matching 
graph generated automatically by stim. `stimcircuits.generate_circuit` can also generate toric code circuits, 
which are not provided as example circuits in Stim.
