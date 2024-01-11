from typing import List

import pytest
from aoc.day_05 import Day05

from resources import read_as_string_list, file_exists

local_test =  file_exists('test/day05.in')
aoc_input = Day05(read_as_string_list('test/day05.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    (['ugknbfddgicrmopn', 'aaa'], 2),
    (['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'], 0),
])
def test_solve_1_examples(test_input: List[str], expected: int):
    assert Day05(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 255


@pytest.mark.parametrize("test_input, expected", [
    (['qjhvhtzxzqqjkmpb', 'xxyxx'], 2),
    (['uurcxstgmygtbstg', 'ieodomkazucvgmuy'], 0),
])
def test_solve_2_examples(test_input: List[str], expected: int):
    assert Day05(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 55
