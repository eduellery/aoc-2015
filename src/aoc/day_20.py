from typing import Generator


class Day20:
    def __init__(self, minimum: int):
        self.minimum = minimum
        self.presents = minimum // 10

    def part1(self) -> Generator[int, None, None]:
        houses = [0] * self.presents
        for e in range(1, self.presents):
            for h in range(e, self.presents, e):
                houses[h] += e

        for i, h in enumerate(houses):
            if h >= self.presents:
                yield i

    def solve1(self) -> int:
        return next(self.part1())

    def part2(self) -> Generator[int, None, None]:
        houses = [0] * self.minimum
        for e in range(1, self.presents):
            for i in range(50):
                idx = e + i * e
                if idx >= self.minimum:
                    break
                houses[idx] += 11 * e

        for i, h in enumerate(houses):
            if h >= self.minimum:
                yield i

    def solve2(self) -> int:
        return next(self.part2())
