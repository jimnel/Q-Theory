# See here for test conventions:
# https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery

import numpy as np
import pytest
import heisenberg as qh


@pytest.mark.parametrize(
    "operator", [qh.I, qh.X, qh.Y, qh.Z]
)
def test_pauli_unitary(operator):
    assert operator.dtype == np.complex64
    assert np.allclose(operator @ operator, np.eye(2))