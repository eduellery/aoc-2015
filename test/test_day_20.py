import pytest
from aoc.day_20 import Day20

aoc_input: int = 29_000_000


@pytest.mark.parametrize("test_input, expected", [
    (30, 2),
    (40, 3),
    (50, 4),
    (60, 4),
    (70, 4),
    (80, 6),
    (90, 6),
    (100, 6),
    (120, 6),
    (140, 8),
    (160, 10),
    (180, 10),
    (200, 12),
])
def test_solve_1_examples(test_input: int, expected: int):
    assert Day20(test_input).solve1() == expected


def test_solve_1_input():
    assert Day20(aoc_input).solve1() == 665_280


@pytest.mark.parametrize("test_input, expected", [
    (30, 2),
    (40, 3),
    (50, 4),
    (60, 4),
    (70, 4),
    (80, 6),
    (90, 6),
    (100, 6),
    (120, 6),
    (140, 8),
    (160, 8),
    (180, 10),
    (200, 12),
])
def test_solve_2_examples(test_input: int, expected: int):
    assert Day20(test_input).solve2() == expected


def test_solve_2_input():
    assert Day20(aoc_input).solve2() == 705_600
