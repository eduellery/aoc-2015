class Day19:
    def __init__(self, text: str):
        lines, self.medicine = text.split('\n\n')
        self.reactions = []
        for line in lines.splitlines():
            before, after = line.split(' => ')
            self.reactions.append((before, after))

    def solve1(self) -> int:
        output = set()
        for replacement in self.reactions:
            pos = ([m for m in range(len(self.medicine)) if self.medicine.startswith(replacement[0], m)])
            for idx in pos:
                output.add((self.medicine[:idx] + replacement[1] + self.medicine[idx + len(replacement[0]):]))
        return len(output)

    def solve2(self) -> int:
        n = 0
        m = self.medicine
        while m != "e":
            for reactant, products in sorted(self.reactions):
                if "".join(products) in m:
                    m = m.replace("".join(products), reactant, 1)
                    n = n + 1
        return n
