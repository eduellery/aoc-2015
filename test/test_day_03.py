import pytest
from aoc.day_03 import Day03

from resources import read_as_string

aoc_input = Day03(read_as_string('test/day03.in'))


@pytest.mark.parametrize("test_input, expected", [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day03(list(test_input)).solve1() == expected


def test_solve_1_input():
    assert aoc_input.solve1() == 2_565


@pytest.mark.parametrize("test_input, expected", [
    ('^v', 3),
    ('^>v<', 3),
    ('^v^v^v^v^v', 11),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day03(test_input).solve2() == expected


def test_solve_2_input():
    assert aoc_input.solve2() == 2_639
