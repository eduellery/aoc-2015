from aoc.day_07 import Day07

from resources import read_as_string_list

aoc_input = Day07(read_as_string_list('test/day07.in'))


def test_solve_1_input():
    assert aoc_input.solve1() == 16_076


def test_solve_2_input():
    assert aoc_input.solve2() == 2_797
