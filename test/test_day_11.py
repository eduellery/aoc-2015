import pytest

from aoc.day_11 import Day11

aoc_input = Day11('hxbxwxba')


@pytest.mark.parametrize("test_input, expected", [
    ('abcdefgh', 'abcdffaa'),
    ('ghijklmn', 'ghjaabcc'),
])
def test_solve_1_examples(test_input: str, expected: str):
    assert Day11(test_input).solve1() == expected


def test_solve_1_input():
    assert aoc_input.solve1() == 'hxbxxyzz'


def test_solve_2_input():
    assert aoc_input.solve2() == 'hxcaabcc'
