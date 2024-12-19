import pytest
from resources import file_exists, read_as_string_list

from day_23 import Day23

test_input = Day23(read_as_string_list('test/res/day23.example'))
local_test =  file_exists('test/res/day23.in')
aoc_input = Day23(read_as_string_list('test/res/day23.in')) if local_test else None


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
