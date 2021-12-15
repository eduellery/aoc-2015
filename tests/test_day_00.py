import pytest
from aoc.day_00 import solve_1, solve_2


@pytest.mark.parametrize("test_input, expected", [
    (1, 1),
    (2, 1),
])
def test_solve_1(test_input, expected):
    assert solve_1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (1, 2),
    (2, 2),
])
def test_solve_2(test_input, expected):
    assert solve_2(test_input) == expected
