import numpy as np

def creation_op(dim):
    coefs = np.sqrt(np.arange(1, dim))
    return np.diag(coefs, k=-1)

def annihilation_op(dim):
    coefs = np.sqrt(np.arange(1, dim))
    return np.diag(coefs, k=1)

def _beam_splitter_matrix(dim):
    return np.kron(creation_op(dim), annihilation_op(dim)) - np.kron(annihilation_op(dim), creation_op(dim))

def beam_splitter_hamiltonian(theta, dim):
    return -1j * theta * _beam_splitter_matrix(dim)

def beam_splitter(theta, dim):
    return expm(theta * _beam_splitter_matrix(dim))