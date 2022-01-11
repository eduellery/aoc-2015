import pytest
from aoc.day_12 import Day12

from resources import read_as_string

aoc_input = Day12(read_as_string('test/day12.in'))


@pytest.mark.parametrize("test_input, expected", [
    ('[1,2,3]', 6),
    ('{"a":2,"b":4}', 6),
    ('[[[3]]]', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ('[]', 0),
    ('{}', 0),
])
def test_solve_1_examples(test_input: str, expected: int):
    assert Day12(test_input).solve1() == expected


def test_solve_1_input():
    assert aoc_input.solve1() == 156_366


@pytest.mark.parametrize("test_input, expected", [
    ('[1,2,3]', 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('[1,"red",5]', 6),
])
def test_solve_2_examples(test_input: str, expected: int):
    assert Day12(test_input).solve2() == expected


def test_solve_2_input():
    assert aoc_input.solve2() == 96_852
