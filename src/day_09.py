from itertools import permutations
from re import findall


class Day09:
    def __init__(self, costs: list[str]):
        distances = {}
        cities = set()

        for cost in costs:
            travel = findall(r'(.*)\sto\s(.*)\s=\s(.*)', cost)
            for orig, dest, dist in travel:
                distances[orig, dest] = dist
                distances[dest, orig] = dist
                cities.add(orig)
                cities.add(dest)

        self.minimum = 10 ** 15
        self.maximum = 0

        for path in permutations(cities):
            current = 0
            for i in range(1, len(path)):
                current += int(distances[path[i - 1], path[i]])
            if current < self.minimum:
                self.minimum = current
            if current > self.maximum:
                self.maximum = current

    def solve1(self) -> int:
        return self.minimum

    def solve2(self) -> int:
        return self.maximum
