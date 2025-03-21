"""
Module for Pauli operators
"""
import numpy as np
from .operator import Operator

I = Operator([[1, 0], [0, 1]])
X = Operator([[0, 1], [1, 0]])
Y = Operator([[0, -1j], [1j, 0]])
Z = Operator([[1, 0], [0, -1]])

pauli_dict = {"I": I, "X": X, "Y": Y, "Z": Z}

# def rotation(theta, axis):
#     """
#     Perform a rotation through angle theta about a given axis.
#     """
#     return np.cos(0.5 * theta) * I -1j * np.sin(0.5 * theta) * pauli_dict[axis]
