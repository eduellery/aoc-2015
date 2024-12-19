import pytest
from resources import file_exists, read_as_string_list

from day_14 import Day14

local_test =  file_exists('test/res/day14.in')
test_input = Day14(['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                    'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'],
                   1000)
aoc_input = Day14(read_as_string_list('test/res/day14.in')) if local_test else None


def test_solve_1_example():
    assert test_input.solve1() == 1_120


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 2_660


def test_solve_2_example():
    assert test_input.solve2() == 689


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 1_256
