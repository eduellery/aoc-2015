import pytest

from resources import file_exists, read_as_string
from src.day_01 import Day01

local_test =  file_exists('test/day01.in')
aoc_input = Day01(read_as_string('test/day01.in')) if local_test else None

@pytest.mark.parametrize("test_input, expected", [
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('()()', 0),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
    (')())())', -3),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day01(test_input).solve1() == expected

@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 280


@pytest.mark.parametrize("test_input, expected", [
    (')', 1),
    ('()())', 5),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day01(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 1_797
