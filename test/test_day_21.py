from aoc.day_21 import Day21

test_input = Day21(8, 12, 7, 2)
aoc_input = Day21(100, 100, 8, 2)


def test_solve_1_example():
    assert test_input.solve1() == 65


def test_solve_1_input():
    assert aoc_input.solve1() == 91


def test_solve_2_example():
    assert test_input.solve2() == 188


def test_solve_2_input():
    assert aoc_input.solve2() == 158
