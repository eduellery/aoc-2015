from typing import List

import pytest
from aoc.day_06 import Day06

from resources import read_as_string_list

aoc_input = Day06(read_as_string_list('test/day06.in'))


def test_solve_1_examples():
    test: List[str] = ['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500']
    assert Day06(test).solve1() == 998_996


def test_solve_1_input():
    assert aoc_input.solve1() == 377_891


@pytest.mark.parametrize("test_input, expected", [
    (['turn on 0,0 through 0,0'], 1),
    (['toggle 0,0 through 999,999'], 2_000_000),
])
def test_solve_2_examples(test_input: List[str], expected: int):
    assert Day06(test_input).solve2() == expected


def test_solve_2_input():
    assert aoc_input.solve2() == 14_110_788
