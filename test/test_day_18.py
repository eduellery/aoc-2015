import pytest
from resources import file_exists, read_as_string_list

from day_18 import Day18

local_test =  file_exists('res/day18.in')
test_input = ['.#.#.#',
              '...##.',
              '#....#',
              '..#...',
              '#.#..#',
              '####..']
aoc_input = Day18(read_as_string_list('res/day18.in')) if local_test else None


def test_solve_1_example():
    assert Day18(test_input, 3).solve1() == 4


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 814


def test_solve_2_example():
    assert Day18(test_input, 5).solve2() == 17


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 924
