import pytest
from aoc.day_10 import Day10

from resources import read_as_string, file_exists

local_test =  file_exists('test/day10.in')
aoc_input = Day10(read_as_string('test/day10.in')) if local_test else None


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 492_982


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 6_989_950
