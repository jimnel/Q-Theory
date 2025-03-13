import numpy as np

I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])

pauli_dict = {"I": I, "X": X, "Y": Y, "Z": Z}

def rotation(theta, axis):
    return np.cos(0.5 * theta) * I -1j * np.sin(0.5 * theta) * pauli_dict[axis]
