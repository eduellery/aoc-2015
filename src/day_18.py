from copy import deepcopy

DIRECTIONS = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x != 0 or y != 0)]


class Day18:
    def __init__(self, lines: list[str], steps: int = 100):
        self.original = {}
        self.size = len(lines)
        self.steps = steps
        for row, line in enumerate(lines):
            for column, char in enumerate(line):
                self.original[(row, column)] = char

    def cycle(self, grid, corners):
        for _ in range(self.steps):
            grid = self.next(grid, corners)
        return grid

    def next(self, grid, corners):
        new_grid = {}
        for (row, column) in grid:
            n = self.count_neighbors(grid, row, column)
            if grid[(row, column)] == '#' and (n == 2 or n == 3) or grid[(row, column)] == '.' and n == 3:
                new_grid[(row, column)] = '#'
            else:
                new_grid[(row, column)] = '.'
        if corners:
            self.set_corners(new_grid)
        return new_grid

    def set_corners(self, grid):
        grid[(0, 0)] = '#'
        grid[(0, self.size - 1)] = '#'
        grid[(self.size - 1, 0)] = '#'
        grid[(self.size - 1, self.size - 1)] = '#'

    def count_neighbors(self, grid, row, column, count: int = 0):
        for (x, y) in DIRECTIONS:
            if not ((0 <= x + row < self.size) and (0 <= y + column < self.size)):
                continue
            if grid[(row + x, column + y)] == '#':
                count += 1
        return count

    @staticmethod
    def count_total(grid, count: int = 0) -> int:
        for v in grid.values():
            if v == '#':
                count += 1
        return count

    def solve1(self) -> int:
        grid = self.cycle(deepcopy(self.original), False)
        return self.count_total(grid)

    def solve2(self) -> int:
        replacement = deepcopy(self.original)
        self.set_corners(replacement)
        grid = self.cycle(replacement, True)
        return self.count_total(grid)
