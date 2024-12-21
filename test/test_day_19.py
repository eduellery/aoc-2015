import pytest
from resources import file_exists, read_as_text

from day_19 import Day19

local_test =  file_exists('res/day19.in')
test1_input = Day19(read_as_text('res/day19.part1.example'))
test2_input = Day19(read_as_text('res/day19.part2.example'))
aoc_input = Day19(read_as_text('res/day19.in')) if local_test else None


def test_solve_1_example():
    assert test1_input.solve1() == 4


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 535


def test_solve_2_example():
    assert test2_input.solve2() == 3


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 212
