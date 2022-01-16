from aoc.day_19 import Day19

from resources import read_as_text

test1_input = Day19(read_as_text('test/day19.part1.example'))
test2_input = Day19(read_as_text('test/day19.part2.example'))
aoc_input = Day19(read_as_text('test/day19.in'))


def test_solve_1_example():
    assert test1_input.solve1() == 4


def test_solve_1_input():
    assert aoc_input.solve1() == 535


def test_solve_2_example():
    assert test2_input.solve2() == 3


def test_solve_2_input():
    assert aoc_input.solve2() == 212
