from typing import List

import pytest
from aoc.day_02 import Day02

from resources import read_as_string_list

aoc_input: List[str] = read_as_string_list('tests/day02.in')


@pytest.mark.parametrize("test_input, expected", [
    (['2x3x4'], 58),
    (['1x1x10'], 43),
])
def test_solve_1_examples(test_input: List[str], expected: int):
    assert Day02(test_input).solve1() == expected


def test_solve_1_input():
    assert Day02(aoc_input).solve1() == 1_598_415


@pytest.mark.parametrize("test_input, expected", [
    (['2x3x4'], 34),
    (['1x1x10'], 14),
])
def test_solve_2_examples(test_input: List[str], expected: int):
    assert Day02(test_input).solve2() == expected


def test_solve_2_input():
    assert Day02(aoc_input).solve2() == 3_812_909
