import pytest
from aoc.day_22 import Day22

from resources import file_exists

local_test =  file_exists('test/day22.in')
aoc_input = Day22(50, 500, 71, 10)


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 1_824


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 1_937
