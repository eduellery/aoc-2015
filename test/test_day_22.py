from aoc.day_22 import Day22

aoc_input = Day22(50, 500, 71, 10)


def test_solve_1_input():
    assert aoc_input.solve1() == 1_824


def test_solve_2_input():
    assert aoc_input.solve2() == 1_937
