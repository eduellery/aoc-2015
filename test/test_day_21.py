import pytest
from resources import file_exists

from day_21 import Day21

local_test =  file_exists('res/day21.in')
test_input = Day21(8, 12, 7, 2)
aoc_input = Day21(100, 100, 8, 2)


def test_solve_1_example():
    assert test_input.solve1() == 65


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 91


def test_solve_2_example():
    assert test_input.solve2() == 188


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 158
