import numpy as np

class Operator:
    def __init__(self, operator):
        self.operator = np.array(operator, dtype=np.complex64)
        assert len(self.operator.shape) == 2
        assert self.operator.shape[0] == self.operator.shape[1]

    def is_hermitian(self):
        return np.allclose(self.operator, self.dag())

    def dag(self):
        return np.conj(self.operator).T

    def __repr__(self):
        return f"{self.operator}"

def kron_list(arr_list):
    result = arr_list[0]
    for op in arr_list[1:]:
        result = np.kron(result, op)
    return result


# def string_to_op(op_str):
#     op_list = [op_dict[s] for s in op_str]
#     return Operator(kron_list(op_list))