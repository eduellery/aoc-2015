from aoc.day_13 import Day13
from resources import read_as_string_list

test_day = Day13(read_as_string_list('test/day13.example'))
input_day = Day13(read_as_string_list('test/day13.in'))


def test_solve_1_example():
    assert test_day.solve1() == 330


def test_solve_1_input():
    assert input_day.solve1() == 618


def test_solve_2_input():
    assert input_day.solve2() == 601
