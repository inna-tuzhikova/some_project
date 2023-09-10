import pytest

from some_project.utils import double, triple


@pytest.mark.parametrize('n,expected', [(0, 0), (1, 2), (-333, -666)])
def test_double(n, expected):
    assert double(n) == expected


@pytest.mark.parametrize('n,expected', [(0, 0), (1, 3), (-333, -999)])
def test_triple(n, expected):
    assert triple(n) == expected
