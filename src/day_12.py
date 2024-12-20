from json import loads


class Day12:
    def __init__(self, doc: str):
        self.doc = doc

    @staticmethod
    def find(i, ignore_red: bool = False) -> int:
        if type(i) is int:
            return i
        if type(i) is list:
            return sum([Day12.find(i, ignore_red) for i in i])
        if type(i) is not dict:
            return 0
        if ignore_red and 'red' in i.values():
            return 0
        return Day12.find(list(i.values()), ignore_red)

    def solve1(self) -> int:
        return self.find(loads(self.doc))

    def solve2(self) -> int:
        return self.find(loads(self.doc), True)
