from re import findall
from typing import List


class Day15:
    def __init__(self, stats: List[str], short: bool = False):
        regex = r'^\w+: capacity ([-\d]+), durability ([-\d]+), flavor ([-\d]+), texture ([-\d]+), calories ([-\d]+)$'

        capacity = []
        durability = []
        flavor = []
        texture = []
        calories = []

        for stat in stats:
            cap, d, f, t, cal = findall(regex, stat)[0]
            capacity.append(int(cap))
            durability.append(int(d))
            flavor.append(int(f))
            texture.append(int(t))
            calories.append(int(cal))

        self.score1 = 0
        self.score2 = 0

        if short:
            self.short_ingredients(calories, capacity, durability, flavor, texture)
        else:
            self.long_ingredients(calories, capacity, durability, flavor, texture)

    def short_ingredients(self, calories, capacity, durability, flavor, texture):
        for i in range(0, 100):
            idx = 100 - i
            cap = capacity[0] * i + capacity[1] * idx
            d = durability[0] * i + durability[1] * idx
            f = flavor[0] * i + flavor[1] * idx
            t = texture[0] * i + texture[1] * idx
            cal = calories[0] * i + calories[1] * idx
            self.set_score(cal, cap, d, f, t)

    def long_ingredients(self, calories, capacity, durability, flavor, texture):
        for i in range(0, 100):
            for j in range(0, 100 - i):
                for k in range(0, 100 - i - j):
                    idx = 100 - i - j - k
                    cap = capacity[0] * i + capacity[1] * j + capacity[2] * k + capacity[3] * idx
                    d = durability[0] * i + durability[1] * j + durability[2] * k + durability[3] * idx
                    f = flavor[0] * i + flavor[1] * j + flavor[2] * k + flavor[3] * idx
                    t = texture[0] * i + texture[1] * j + texture[2] * k + texture[3] * idx
                    cal = calories[0] * i + calories[1] * j + calories[2] * k + calories[3] * idx
                    self.set_score(cal, cap, d, f, t)

    def set_score(self, cal, cap, d, f, t):
        if cap <= 0 or d <= 0 or f <= 0 or t <= 0:
            return
        score = cap * d * f * t
        if score > self.score1:
            self.score1 = score
        if score > self.score2 and cal == 500:
            self.score2 = score

    def solve1(self) -> int:
        return self.score1

    def solve2(self) -> int:
        return self.score2
