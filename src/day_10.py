from itertools import groupby


class Day10:
    def __init__(self, seed: str):
        self.seed = seed

    @staticmethod
    def transform(value: str) -> str:
        return ''.join(str(len(list(count))) + val for val, count in groupby(value))

    def loop(self, count: int) -> str:
        value = self.seed
        for _ in range(count):
            value = self.transform(value)
        return value

    def solve1(self) -> int:
        return len(self.loop(40))

    def solve2(self) -> int:
        return len(self.loop(50))
