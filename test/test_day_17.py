from aoc.day_17 import Day17

from resources import read_as_int_list

test_input = Day17([20, 15, 10, 5, 5], 25)
aoc_input = Day17(read_as_int_list('test/day17.in'))


def test_solve_1_example():
    assert test_input.solve1() == 4


def test_solve_1_input():
    assert aoc_input.solve1() == 1_304


def test_solve_2_example():
    assert test_input.solve2() == 3


def test_solve_2_input():
    assert aoc_input.solve2() == 18
