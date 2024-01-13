import pytest
from aoc.day_13 import Day13

from resources import read_as_string_list, file_exists

local_test =  file_exists('test/day13.in')
test_day = Day13(read_as_string_list('test/day13.example'))
input_day = Day13(read_as_string_list('test/day13.in')) if local_test else None


def test_solve_1_example():
    assert test_day.solve1() == 330


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert input_day.solve1() == 618


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert input_day.solve2() == 601
