from copy import deepcopy

spell_cost = {
    'Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Recharge': 229,
    'Poison': 173,
}
spell_damage = {
    'Missile': 4,
    'Drain': 2,
}
spell_health = {
    'Drain': 2,
}
effects_duration = {
    'Shield': 6,
    'Recharge': 5,
    'Poison': 6,
}


class Game:
    def __init__(self, player_health: int, player_mana: int, boss_health: int, boss_dmg: int):
        self.player_health = player_health
        self.player_mana = player_mana
        self.boss_health = boss_health
        self.boss_dmg = boss_dmg

        self.mana_spent = 0
        self.casted_spells: list[str] = []
        self.effects: dict[str, int] = {}

    def cast(self, spell_name):
        if spell_name in spell_damage:
            self.boss_health -= spell_damage[spell_name]
        if spell_name in spell_health:
            self.player_health += spell_health[spell_name]
        if spell_name in effects_duration:
            self.effects[spell_name] = effects_duration[spell_name]

        self.mana_spent += spell_cost[spell_name]
        self.player_mana -= spell_cost[spell_name]
        self.casted_spells.append(spell_name)

    def not_available(self, spell_name):
        return spell_name in [x for x in self.effects] or spell_cost[spell_name] > self.player_mana

    def apply_effects(self):
        for e in self.effects:
            if e == 'Poison':
                self.boss_health -= 3
            elif e == 'Recharge':
                self.player_mana += 101
            self.effects[e] = self.effects[e] - 1
        self.effects = {key: val for key, val in self.effects.items() if val > 0}

    def attack(self):
        damage = self.boss_dmg if 'Shield' not in [ef for ef in self.effects] else self.boss_dmg - 7
        self.player_health -= max(damage, 1)

    def boss_defeated(self):
        return self.boss_health <= 0

    def player_alive(self):
        return self.player_health > 0


class Day22:
    def __init__(self, player_hit: int, mana: int, boss_hit: int, dmg: int):
        self.player_hit = player_hit
        self.mana = mana
        self.boss_hit = boss_hit
        self.dmg = dmg

    def simulate(self, hardcore: bool = False):
        low_score = 10 ** 9
        all_games = [Game(self.player_hit, self.mana, self.boss_hit, self.dmg)]
        while all_games:
            new_games = []
            for game in all_games:
                game.apply_effects()
                game.player_health -= 1 if hardcore else 0
                for spell in spell_cost:
                    if game.not_available(spell):
                        continue
                    new_game = deepcopy(game)
                    new_game.cast(spell)
                    if new_game.mana_spent > low_score:
                        continue
                    new_game.apply_effects()
                    if new_game.boss_defeated() and new_game.mana_spent < low_score:
                        low_score = new_game.mana_spent
                        continue
                    new_game.attack()
                    if new_game.player_alive():
                        new_games.append(new_game)
            all_games = new_games
        return low_score

    def solve1(self):
        return self.simulate()

    def solve2(self):
        return self.simulate(True)
