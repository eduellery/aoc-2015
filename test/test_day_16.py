from aoc.day_16 import Day16

from resources import read_as_string_list

aoc_input = Day16(read_as_string_list('test/day16.in'))


def test_solve_1_input():
    assert aoc_input.solve1() == 40


def test_solve_2_input():
    assert aoc_input.solve2() == 241
