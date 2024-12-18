

class Day08:
    def __init__(self, lines: list[str]):
        self.dec: int = 0
        self.enc: int = 0
        for line in lines:
            self.dec += len(line) - len(bytes(line, "utf-8").decode("unicode_escape")) + 2
            self.enc += line.count('\\') + line.count('"') + 2

    def solve1(self) -> int:
        return self.dec

    def solve2(self) -> int:
        return self.enc
