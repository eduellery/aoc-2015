from aoc.day_10 import Day10

aoc_input: str = '1321131112'


def test_solve_1_input():
    assert Day10(aoc_input).solve1() == 492_982


def test_solve_2_input():
    assert Day10(aoc_input).solve2() == 6_989_950
