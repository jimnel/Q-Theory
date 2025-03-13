# See here for test conventions:
# https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery

def func(x):
    return x + 1

def test_func_1():
    assert func(4) == 5

def test_func_2():
    assert func(3) == 5
