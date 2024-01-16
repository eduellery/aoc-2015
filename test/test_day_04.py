import pytest
from aoc.day_04 import Day04

from resources import read_as_string, file_exists

local_test =  file_exists('test/day04.in')
aoc_input = Day04(read_as_string('test/day04.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    ('abcdef', 609_043),
    ('pqrstuv', 1_048_970),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day04(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 346_386


@pytest.mark.parametrize("test_input, expected", [
    ('abcdef', 6_742_839),
    ('pqrstuv', 5_714_438),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day04(test_input).solve2() == expected


def test_unsolvable_solve_2():
    assert Day04('a' * 16).solve2() == -1


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 9_958_218
