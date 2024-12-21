import pytest
from resources import file_exists, read_as_string_list

from day_13 import Day13

local_test =  file_exists('res/day13.in')
test_day = Day13(read_as_string_list('res/day13.example'))
input_day = Day13(read_as_string_list('res/day13.in')) if local_test else None


def test_solve_1_example():
    assert test_day.solve1() == 330


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert input_day.solve1() == 618


def test_solve_2_example():
    assert test_day.solve2() == 286


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert input_day.solve2() == 601
