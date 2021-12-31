from typing import List

import pytest
from aoc.day_05 import Day05

from resources import read_as_string_list

aoc_input: List[str] = read_as_string_list('test/day05.in')


@pytest.mark.parametrize("test_input, expected", [
    (['ugknbfddgicrmopn', 'aaa'], 2),
    (['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'], 0),
])
def test_solve_1_examples(test_input: List[str], expected: int):
    assert Day05(test_input).solve1() == expected


def test_solve_1_input():
    assert Day05(aoc_input).solve1() == 255


@pytest.mark.parametrize("test_input, expected", [
    (['qjhvhtzxzqqjkmpb', 'xxyxx'], 2),
    (['uurcxstgmygtbstg', 'ieodomkazucvgmuy'], 0),
])
def test_solve_2_examples(test_input: List[str], expected: int):
    assert Day05(test_input).solve2() == expected


def test_solve_2_input():
    assert Day05(aoc_input).solve2() == 55
