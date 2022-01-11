from aoc.day_15 import Day15

from resources import read_as_string_list

test_input = Day15(['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'],
                   True)
aoc_input = Day15(read_as_string_list('test/day15.in'))


def test_solve_1_example():
    assert test_input.solve1() == 62_842_880


def test_solve_1_input():
    assert aoc_input.solve1() == 222_870


def test_solve_2_example():
    assert test_input.solve2() == 57_600_000


def test_solve_2_input():
    assert aoc_input.solve2() == 117_936
