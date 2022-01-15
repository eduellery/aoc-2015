from aoc.day_18 import Day18

from resources import read_as_string_list

test_input = ['.#.#.#',
              '...##.',
              '#....#',
              '..#...',
              '#.#..#',
              '####..']
aoc_input = Day18(read_as_string_list('test/day18.in'))


def test_solve_1_example():
    assert Day18(test_input, 3).solve1() == 4


def test_solve_1_input():
    assert aoc_input.solve1() == 814


def test_solve_2_example():
    assert Day18(test_input, 5).solve2() == 17


def test_solve_2_input():
    assert aoc_input.solve2() == 924
