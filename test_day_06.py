
import pytest

from resources import file_exists, read_as_string_list
from src.day_06 import Day06

local_test =  file_exists('test/day06.in')
aoc_input = Day06(read_as_string_list('test/day06.in')) if local_test else None


def test_solve_1_examples():
    test: list[str] = ['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500']
    assert Day06(test).solve1() == 998_996


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 377_891


@pytest.mark.parametrize("test_input, expected", [
    (['turn on 0,0 through 0,0'], 1),
    (['toggle 0,0 through 999,999'], 2_000_000),
    (['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500'], 1_001_996),
])
def test_solve_2_examples(test_input: list[str], expected: int):
    assert Day06(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 14_110_788
