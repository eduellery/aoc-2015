import pytest
from resources import file_exists, read_as_string

from day_11 import Day11

local_test =  file_exists('test/res/day11.in')
aoc_input = Day11(read_as_string('test/res/day11.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    ('abcdefgh', 'abcdffaa'),
    ('ghijklmn', 'ghjaabcc'),
])
def test_solve_1_examples(test_input: str, expected: str):
    assert Day11(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 'hxbxxyzz'


@pytest.mark.parametrize("test_input, expected", [
    ('abcdefgh', 'abcdffbb'),
    ('ghijklmn', 'ghjbbcdd'),
])
def test_solve_2_examples(test_input: str, expected: str):
    assert Day11(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 'hxcaabcc'
