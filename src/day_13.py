from itertools import permutations
from re import findall


class Day13:
    def __init__(self, happiness: list[str]):
        self.happiness = happiness

    def populate(self) -> tuple[dict[str, int], set[str]]:
        match = {}
        people = set()

        for h in self.happiness:
            a, signal, number, b = findall(r'(\w+) \w+ (\w+) (\d+) .* (\w+)\.', h)[0]
            match[a + b] = int(number) * (1 if signal == 'gain' else -1)
            people.add(a)

        return match, people

    @staticmethod
    def cost(match: dict[str, int], person: tuple[str, ...]) -> int:
        size = len(person)
        gain = 0
        for i in range(size):
            gain += match[person[i] + person[i - 1]]
            gain += match[person[i] + person[(i + 1) % size]]
        return gain

    def solve1(self) -> int:
        match, people = self.populate()

        return max([self.cost(match, p) for p in permutations(people)])

    def solve2(self) -> int:
        match, people = self.populate()

        for person in people:
            match[person + 'me'] = 0
            match['me' + person] = 0
        people.add('me')

        return max([self.cost(match, p) for p in permutations(people)])
