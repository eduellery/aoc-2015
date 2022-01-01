from re import findall
from typing import List

ON = 'turn on'
OFF = 'turn off'
TOGGLE = 'toggle'


class Day06:
    def __init__(self, instructions: List[str]):
        self.instructions = instructions

    def solve1(self) -> int:
        lights = [[0 for _ in range(1000)] for _ in range(1000)]
        for instruction in self.instructions:
            values = findall(r'(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)', instruction)
            for action, x_min, y_min, x_max, y_max in values:
                pos = [(x, y) for x in range(int(x_min), int(x_max) + 1) for y in range(int(y_min), int(y_max) + 1)]
                for x, y in pos:
                    if action == ON:
                        lights[x][y] = 1
                    elif action == OFF:
                        lights[x][y] = 0
                    elif action == TOGGLE:
                        lights[x][y] = 1 - lights[x][y]
        return sum(map(sum, lights))

    def solve2(self) -> int:
        lights = [[0 for _ in range(1000)] for _ in range(1000)]
        for instruction in self.instructions:
            values = findall(r'(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)', instruction)
            for action, x_min, y_min, x_max, y_max in values:
                pos = [(x, y) for x in range(int(x_min), int(x_max) + 1) for y in range(int(y_min), int(y_max) + 1)]
                for x, y in pos:
                    if action == ON:
                        lights[x][y] += 1
                    elif action == OFF and lights[x][y] > 0:
                        lights[x][y] -= 1
                    elif action == TOGGLE:
                        lights[x][y] += 2
        return sum(map(sum, lights))
