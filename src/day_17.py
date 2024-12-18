from itertools import combinations
from typing import List


class Day17:
    def __init__(self, numbers: List[int], capacity: int = 150):
        self.combinations = [z for i in range(len(numbers)) for z in combinations(numbers, i) if sum(z) == capacity]

    def solve1(self) -> int:
        return len(self.combinations)

    def solve2(self) -> int:
        return len([x for x in self.combinations if len(x) == min([len(x) for x in self.combinations])])
