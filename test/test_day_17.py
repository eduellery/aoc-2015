import pytest
from resources import file_exists, read_as_int_list

from day_17 import Day17

local_test =  file_exists('res/day17.in')
test_input = Day17([20, 15, 10, 5, 5], 25)
aoc_input = Day17(read_as_int_list('res/day17.in')) if local_test else None


def test_solve_1_example():
    assert test_input.solve1() == 4


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 1_304


def test_solve_2_example():
    assert test_input.solve2() == 3


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 18
