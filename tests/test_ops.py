import pytest

from some_project.utils.ops import add, mul


@pytest.mark.parametrize('a,b,expected', [(0, 0, 0), (1, 1, 2), (-3, 1, -2)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize('a,b,expected', [(0, 0, 0), (1, 1, 1), (5, 5, 25)])
def test_mul(a, b, expected):
    assert mul(a, b) == expected
