import pytest
from aoc.day_07 import Day07

from resources import read_as_string_list, file_exists

test1_input = Day07(read_as_string_list('test/day07.part1.example'))
test2_input = Day07(read_as_string_list('test/day07.part2.example'))
local_test =  file_exists('test/day07.in')
aoc_input = Day07(read_as_string_list('test/day07.in')) if local_test else None


def test_solve_1_example():
    assert test1_input.solve1() == 123


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 16_076


def test_solve_2_example():
    assert test2_input.solve2() == 4616


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 2_797
