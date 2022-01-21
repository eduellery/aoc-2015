from aoc.day_23 import Day23

from resources import read_as_string_list

aoc_input = Day23(read_as_string_list('test/day23.in'))


def test_solve_1_input():
    assert aoc_input.solve1() == 184


def test_solve_2_input():
    assert aoc_input.solve2() == 231
