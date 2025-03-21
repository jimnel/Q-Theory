import numpy as np

class ConstantSampling:
    def __init__(self, final_time, sample_count, initial_time=0.):
        self.final_time = final_time
        self.initial_time = initial_time
        self.sample_count = sample_count
        self.delta = (final_time - initial_time) / sample_count

    def get_grid(self):
        _ts = np.linspace(self.initial_time, self.final_time, self.sample_count+1)
        assert np.isclose(_ts[1] - _ts[0], self.delta)
        return _ts


class BaseHamiltonian:
    def __init__(self, dim):
        self.dim = dim

    def sample(self, t):
        return NotImplementedError
