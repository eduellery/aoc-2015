import pytest
from resources import file_exists, read_as_string

from day_03 import Day03

local_test =  file_exists('res/day03.in')
aoc_input = Day03(read_as_string('res/day03.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day03(list(test_input)).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 2_565


@pytest.mark.parametrize("test_input, expected", [
    ('^v', 3),
    ('^>v<', 3),
    ('^v^v^v^v^v', 11),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day03(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 2_639
