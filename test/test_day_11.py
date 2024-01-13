import pytest
from aoc.day_11 import Day11

from resources import read_as_string, file_exists

local_test =  file_exists('test/day11.in')
aoc_input = Day11(read_as_string('test/day11.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    ('abcdefgh', 'abcdffaa'),
    ('ghijklmn', 'ghjaabcc'),
])
def test_solve_1_examples(test_input: str, expected: str):
    assert Day11(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 'hxbxxyzz'


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 'hxcaabcc'
