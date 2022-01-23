class Day25:
    def __init__(self, row: int, col: int):
        self.row = row - 1
        self.col = col - 1

    def solve1(self) -> int:
        tri = self.row + self.col
        start = (tri * tri + tri) // 2
        delta = self.col if tri % 2 else self.row
        return (20151125 * pow(252533, start + delta, 33554393)) % 33554393

    def solve2(self) -> int:
        return self.row + self.col + 2
