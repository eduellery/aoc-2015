import pytest
from aoc.day_07 import Day07

from resources import read_as_string_list, file_exists

local_test =  file_exists('test/day07.in')
aoc_input = Day07(read_as_string_list('test/day07.in')) if local_test else None


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 16_076


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 2_797
