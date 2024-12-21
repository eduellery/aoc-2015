import pytest
from resources import file_exists, read_as_string_list

from day_16 import Day16

test_input = Day16(['Sue 1: goldfish: 9, cars: 0, samoyeds: 9',
                    'Sue 2: vizslas: 0, cats: 7, akitas: 0',
                    'Sue 3: cars: 2, pomeranians: 1, samoyeds: 2'])
local_test =  file_exists('res/day16.in')
aoc_input = Day16(read_as_string_list('res/day16.in')) if local_test else None


def test_solve_1_example():
    assert test_input.solve1() == 2


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 40


def test_solve_2_example():
    assert test_input.solve2() == 3


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 241
