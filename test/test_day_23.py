import pytest
from aoc.day_23 import Day23

from resources import read_as_string_list, file_exists

test_input = Day23(read_as_string_list('test/day23.example'))
local_test =  file_exists('test/day23.in')
aoc_input = Day23(read_as_string_list('test/day23.in')) if local_test else None


def test_solve_1_example():
    assert test_input.solve1() == 27


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 184


def test_solve_2_example():
    assert test_input.solve2() == 81


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() 