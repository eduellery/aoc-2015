from typing import List

import pytest
from src.day_24 import Day24

from resources import read_as_int_list, file_exists

local_test =  file_exists('test/day24.in')
aoc_input = Day24(read_as_int_list('test/day24.in')) if local_test else None


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3, 4, 5, 7, 8, 9, 10, 11],99),
    ([1, 4, 5, 11, 13, 17, 19, 23, 29],319),
])
def test_solve_1_examples(test_input: List[str], expected: int):
    assert Day24(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 10_439_961_859


def test_solve_2_example():
    assert Day24([1, 4, 5, 11, 13, 17, 19, 23, 29]).solve2() == 29


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 72_050_269
