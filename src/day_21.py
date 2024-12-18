from collections import namedtuple
from copy import copy
from itertools import chain, combinations, product
from typing import Tuple, Generator

Thing = namedtuple('Thing', 'name cost damage armor')

WEAPONS = [
    Thing('Dagger', 8, 4, 0),
    Thing('Shortsword', 10, 5, 0),
    Thing('Warhammer', 25, 6, 0),
    Thing('Longsword', 40, 7, 0),
    Thing('Greataxe', 74, 8, 0),
]

ARMOR = [
    Thing('Leather', 13, 0, 1),
    Thing('Chainmail', 31, 0, 2),
    Thing('Splintmail', 53, 0, 3),
    Thing('Bandedmail', 75, 0, 4),
    Thing('Platemail', 102, 0, 5),
]

RINGS = [
    Thing('Damage +1', 25, 1, 0),
    Thing('Damage +2', 50, 2, 0),
    Thing('Damage +3', 100, 3, 0),
    Thing('Defense +1', 20, 0, 1),
    Thing('Defense +2', 40, 0, 2),
    Thing('Defense +3', 80, 0, 3),
]


class Player:
    def __init__(self, name, hit, damage, armor):
        self.name = name
        self.hit = hit
        self.damage = damage
        self.armor = armor

    def defend(self, other):
        self.hit -= max(1, other.damage - self.armor)

    def dead(self):
        return self.hit <= 0


class Day21:
    def __init__(self, player_hit: int, boss_hit: int, dmg: int, armor: int):
        self.boss = Player('Boss', boss_hit, dmg, armor)
        self.player_hit = player_hit

    @staticmethod
    def play(you, boss):
        while True:
            boss.defend(you)
            if boss.dead():
                return you
            you.defend(boss)
            if you.dead():
                return boss

    @staticmethod
    def inventories():
        weapons = chain.from_iterable(combinations(WEAPONS, n) for n in range(1, 2))
        armor = chain.from_iterable(combinations(ARMOR, n) for n in range(0, 2))
        rings = chain.from_iterable(combinations(RINGS, n) for n in range(0, 3))

        return map(
            lambda inv: list(inv[0] + inv[1] + inv[2]),
            product(weapons, armor, rings)
        )

    @staticmethod
    def players(name, hit, inventories):
        for inv in inventories:
            spent = sum(i.cost for i in inv)
            player = Player(
                name,
                hit,
                damage=sum(i.damage for i in inv),
                armor=sum(i.armor for i in inv),
            )
            yield spent, player

    def outcomes(self, inventories):
        for spent, you in Day21.players('You', self.player_hit, inventories):
            winner = Day21.play(you, copy(self.boss))
            yield spent, you, winner is you

    def winning(self, inventories) -> Generator[Tuple[int, Player], None, None]:
        return ((spent, you) for spent, you, outcome in self.outcomes(inventories) if outcome is True)

    def losing(self, inventories) -> Generator[Tuple[int, Player], None, None]:
        return ((spent, you) for spent, you, outcome in self.outcomes(inventories) if outcome is False)

    def solve1(self) -> int:
        spent, _ = min(self.winning(Day21.inventories()))
        return spent

    def solve2(self) -> int:
        spent, _ = max(self.losing(Day21.inventories()))
        return spent
