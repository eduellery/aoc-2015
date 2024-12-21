import pytest
from resources import file_exists, read_as_string

from day_12 import Day12

local_test =  file_exists('res/day12.in')
aoc_input = Day12(read_as_string('res/day12.in')) if local_test else None


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


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
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


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 96_852
