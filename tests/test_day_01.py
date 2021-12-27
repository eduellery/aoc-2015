import pytest
from resources import read_as_string
from aoc.day_01 import Day01

day01_input: str = read_as_string('/Users/eehilti/Developer/repositories/github/aoc-2015/tests/day01.in')


@pytest.mark.parametrize("test_input, expected", [
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('()()', 0),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
    (')())())', -3),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day01(test_input).solve1() == expected


def test_solve_1_input():
    assert Day01(day01_input).solve1() == 280


@pytest.mark.parametrize("test_input, expected", [
    (')', 1),
    ('()())', 5),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day01(test_input).solve2() == expected


def test_solve_2_input():
    assert Day01(day01_input).solve2() == 1_797
