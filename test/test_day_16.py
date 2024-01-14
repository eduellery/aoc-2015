import pytest
from aoc.day_16 import Day16

from resources import read_as_string_list, file_exists

local_test =  file_exists('test/day16.in')
aoc_input = Day16(read_as_string_list('test/day16.in')) if local_test else None


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 40


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 241
