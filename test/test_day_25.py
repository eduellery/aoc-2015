from aoc.day_25 import Day25

aoc_input = Day25(3_010, 3_019)


def test_solve_1_input():
    assert aoc_input.solve1() == 8_997_277


def test_solve_2_input():
    assert aoc_input.solve2() == 6_029
