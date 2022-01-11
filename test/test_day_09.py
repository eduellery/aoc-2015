from aoc.day_09 import Day09

from resources import read_as_string_list

test_day = Day09(['London to Dublin = 464', 'London to Belfast = 518', 'Dublin to Belfast = 141'])
input_day = Day09(read_as_string_list('test/day09.in'))


def test_solve_1_example():
    assert test_day.solve1() == 605


def test_solve_1_input():
    assert input_day.solve1() == 117


def test_solve_2_example():
    assert test_day.solve2() == 982


def test_solve_2_input():
    assert input_day.solve2() == 909
