

class Day02:
    def __init__(self, lines: list[str]):
        self.lines = lines

    def solve1(self, area: int = 0) -> int:
        for line in self.lines:
            x, y, z = sorted(map(int, line.split('x')))
            area += 2 * (x * y + x * z + y * z) + x * y
        return area

    def solve2(self, ribbon: int = 0) -> int:
        for line in self.lines:
            x, y, z = sorted(map(int, line.split('x')))
            ribbon += x + x + y + y + x * y * z
        return ribbon
