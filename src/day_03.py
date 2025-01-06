

class Day03:
    def __init__(self, directions: str):
        self.directions = directions

    @staticmethod
    def move(santa: tuple[int, int], direction: str):
        x, y = santa
        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y += 1
        else: # direction == 'v'
            y -= 1
        return x, y

    def visited_houses(self, directions: str) -> set[tuple[int, int]]:
        houses: set[tuple[int, int]] = set()
        santa: tuple[int, int] = (0, 0)
        houses.add(santa)
        for direction in directions:
            santa = self.move(santa, direction)
            houses.add(santa)
        return houses

    def solve1(self) -> int:
        return len(self.visited_houses(self.directions))

    def solve2(self) -> int:
        santa_houses = self.visited_houses(self.directions[0::2])
        robot_houses = self.visited_houses(self.directions[1::2])
        return len(santa_houses | robot_houses)
