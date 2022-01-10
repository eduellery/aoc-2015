from collections import Counter
from itertools import accumulate, cycle
from re import findall
from typing import List


class Day14:
    def __init__(self, descriptions: List[str], seconds: int = 2503):
        self.reindeer_dict = {}
        history = {}

        for description in descriptions:
            reindeer, speed, duration, rest = findall(r'(\w+) .* (\d+) .* (\d+) .* (\d+) \w+\.', description)[0]
            mod = int(duration) + int(rest)
            amount = 0
            distance = 0
            while amount < seconds:
                if amount % mod < int(duration):
                    distance += int(speed)
                amount += 1
            self.reindeer_dict[reindeer] = distance
            steps = cycle([int(speed)] * int(duration) + [0] * int(rest))
            history[reindeer] = list(accumulate(next(steps) for _ in range(seconds)))

        self.scored = [i for a in zip(*history.values()) for i, v in enumerate(a) if v == max(a)]

    def solve1(self) -> int:
        return max(self.reindeer_dict.values())

    def solve2(self) -> int:
        return max(Counter(self.scored).values())
