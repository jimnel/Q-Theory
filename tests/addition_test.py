import pytest
from addition import add

def test_add():
    assert add(1, 2) == 3


def test_add_fail():
    with pytest.raises(TypeError):
        add(1, 'a')


@pytest.mark.parametrize(
    "x,y,result",[(0, 1, 1), (1, 0, 1)]
)
def test_add_many(x, y, result):
    assert add(x, y) == result


@pytest.mark.parametrize("x",[0, 1, 2])
@pytest.mark.parametrize("y",[0, 1, 2])
def test_add_many_2(x, y):
    assert add(x, y) == x + y


@pytest.mark.parametrize(
    "x,y",[('a', 0), (0, 'a')]
)
def test_add_fail_many(x, y):
    with pytest.raises(TypeError):
        add(1, 'a')
