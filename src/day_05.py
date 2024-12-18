from re import findall, search


class Day05:
    def __init__(self, lines: list[str]):
        self.lines = lines

    def solve1(self, nice: int = 0) -> int:
        for line in self.lines:
            if len(findall(r"[aeiou]", line)) >= 3 \
                    and search(r"([a-z])\1", line) \
                    and not search(r"ab|cd|pq|xy", line):
                nice += 1
        return nice

    def solve2(self, nice: int = 0) -> int:
        for line in self.lines:
            if search(r'([a-z]{2}).*\1', line) \
                    and search(r'([a-z]).\1', line):
                nice += 1
        return nice
