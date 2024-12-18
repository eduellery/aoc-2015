import pytest

from resources import file_exists
from src.day_22 import Day22

test_input = Day22(10, 250, 13, 8)
local_test =  file_exists('test/day22.in')
aoc_input = Day22(50, 500, 71, 10)


def test_solve_1_example():
    assert test_input.solve1() == 226


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 1_824


def test_solve_2_example():
    assert test_input.solve2() == 226


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 1_937
