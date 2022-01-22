from aoc.day_24 import Day24

from resources import read_as_int_list

test_input = Day24([1, 2, 3, 4, 5, 7, 8, 9, 10, 11])
aoc_input = Day24(read_as_int_list('test/day24.in'))


def test_solve_1_example():
    assert test_input.solve1() == 99


def test_solve_1_input():
    assert aoc_input.solve1() == 10_439_961_859


def test_solve_2_input():
    assert aoc_input.solve2() == 72_050_269
