import numpy as np

class State:
    def __init__(self, state):
        self.state = np.array(state)
        if len(self.state.shape) == 1:
            self.state = self.state[:, None]
        assert len(self.state.shape) == 2
        assert self.state.shape[1] == 1
        self.dim = self.state.shape[0]

    def probs(self):
        return np.real(np.conj(self.state) * self.state)

    def dag(self):
        return np.conj(self.state).T
        
    def expectation(self, operator):
        return np.real(self.dag() @ (operator.operator @ self.state)).item()
    
    def norm(self):
        return self.probs().sum()
    
    def check_norm(self):
        return np.isclose(self.norm(), 1.0)

    def apply_unitary(self, unitary):
        return State(unitary.operator @ self.state)
    
    def __repr__(self):
        return "".join([f"|{i}>: {self.state[i][0]}\n" for i in range(self.dim)])


def random_state(dim):
    state = np.random.rand(dim) + 1j * np.random.rand(dim)
    state /= np.linalg.norm(state)
    return State(state)


def basis_state(dim, index):
    state = np.zeros(dim)
    state[index] = 1.
    return State(state)
