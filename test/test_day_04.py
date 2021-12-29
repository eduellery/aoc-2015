import pytest
from aoc.day_04 import Day04


@pytest.mark.parametrize("test_input, expected", [
    ('abcdef', 609_043),
    ('pqrstuv', 1_048_970),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day04(test_input).solve1() == expected


def test_solve_1_input():
    assert Day04('iwrupvqb').solve1() == 346_386


def test_solve_2_input():
    assert Day04('iwrupvqb').solve2() == 9_958_218


def test_unsolvable_solve_2():
    assert Day04('a' * 16).solve2() == -1
