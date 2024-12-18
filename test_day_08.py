import pytest

from resources import file_exists, read_as_string_list
from src.day_08 import Day08

test_input = Day08(['""', '"abc"', '"aaa\\"aaa"', '"\\x27"'])
local_test =  file_exists('test/day08.in')
aoc_input = Day08(read_as_string_list('test/day08.in')) if local_test else None


def test_solve_1_example():
    assert test_input.solve1() == 12


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 1_333


def test_solve_2_example():
    assert test_input.solve2() == 19


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 2_046
