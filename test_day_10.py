import pytest
from src.day_10 import Day10

from resources import read_as_string, file_exists

local_test =  file_exists('test/day10.in')
aoc_input = Day10(read_as_string('test/day10.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    ('1', 82_350),
    ('11', 107_312),
    ('21', 139_984),
    ('1211', 182_376),
    ('111221', 237_746),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day10(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 492_982


@pytest.mark.parametrize("test_input, expected", [
    ('1', 1_166_642),
    ('11', 1_520_986),
    ('21', 1_982_710),
    ('1211', 2_584_304),
    ('111221', 3_369_156),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day10(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 6_989_950
