import pytest
from aoc.day_09 import Day09

from resources import read_as_string_list, file_exists

test_day = Day09(read_as_string_list('test/day09.example'))
local_test =  file_exists('test/day09.in')
input_day = Day09(read_as_string_list('test/day09.in')) if local_test else None


def test_solve_1_example():
    assert test_day.solve1() == 605


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert input_day.solve1() == 117


def test_solve_2_example():
    assert test_day.solve2() == 982


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert input_day.solve2() == 909
