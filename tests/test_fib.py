import pytest

from some_project.utils import fib


def test_invalid_value():
    value = -1
    with pytest.raises(ValueError):
        fib(value)


def test_invalid_type():
    value = 'aaa'
    with pytest.raises(TypeError):
        fib(value)


@pytest.mark.parametrize(
    'n,expected',
    [(0, 0), (1, 1), (2, 1), (7, 13), (10, 55), (15, 610)]
)
def test_fib(n, expected):
    assert fib(n) == expected
