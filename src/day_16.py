from collections.abc import Generator

CRITERIA = dict(
    children=3,
    cats=7,
    samoyeds=2,
    pomeranians=3,
    akitas=0,
    vizslas=0,
    goldfish=5,
    trees=3,
    cars=2,
    perfumes=1,
)

COMPARES = dict(
    cats=(lambda a, c: a > c),
    trees=(lambda a, c: a > c),
    pomeranians=(lambda a, c: a < c),
    goldfish=(lambda a, c: a < c),
)


class Day16:
    def __init__(self, aunt_list: list[str]):
        self.aunts: dict[str, dict[str, int]] = {}
        for line in aunt_list:
            name, _, compounds = line.partition(':')
            self.aunts[name] = {}
            for compound in compounds.split(','):
                compound = compound.strip()
                cname, _, amt = compound.partition(':')
                self.aunts[name][cname] = int(amt)

    def find_matches(self, criteria, compares={}) -> Generator[str]:
        for name, aunt in self.aunts.items():
            for k, v in criteria.items():
                compare = compares.get(k, lambda a, c: a == c)
                if k in aunt and not compare(aunt[k], v):
                    break
            else:
                yield name

    def solve1(self) -> int:
        return int(''.join(self.find_matches(CRITERIA)).split()[1])

    def solve2(self) -> int:
        return int(''.join(self.find_matches(CRITERIA, COMPARES)).split()[1])
