from aoc.day_08 import Day08

from resources import read_as_string_list

test_input = Day08(['""', '"abc"', '"aaa\\"aaa"', '"\\x27"'])
aoc_input = Day08(read_as_string_list('test/day08.in'))


def test_solve_1_example():
    assert test_input.solve1() == 12


def test_solve_1_input():
    assert aoc_input.solve1() == 1_333


def test_solve_2_example():
    assert test_input.solve2() == 19


def test_solve_2_input():
    assert aoc_input.solve2() == 2_046
