import pytest
from aoc.day_25 import Day25

from resources import file_exists

local_test =  file_exists('test/day25.in')
aoc_input = Day25(3_010, 3_019)


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 8_997_277


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 6_029
