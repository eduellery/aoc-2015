class Day01:
    def __init__(self, chars: str):
        self.chars = chars

    def solve1(self, count: int = 0) -> int:
        for value in self.chars:
            count += (1 if value == '(' else -1)
        return count

    def solve2(self, count: int = 0, basement_index: int = 0) -> int:
        for index, value in enumerate(self.chars):
            count += (1 if value == '(' else -1)
            if basement_index == 0 and count == -1:
                basement_index = index + 1
        return basement_index
