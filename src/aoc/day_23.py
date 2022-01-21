from re import split
from typing import List, Dict, Any


class Day23:
    def __init__(self, instructions: List[str]):
        self.instructions = instructions

    def hlf(self, registers, register):
        registers[register] //= 2
        return 1, registers

    def tpl(self, registers, register):
        registers[register] *= 3
        return 1, registers

    def inc(self, registers, register):
        registers[register] += 1
        return 1, registers

    def jmp(self, registers, offset):
        return int(offset), registers

    def jie(self, registers, register, offset):
        return int(offset) if registers[register] % 2 == 0 else 1, registers

    def jio(self, registers, register, offset):
        return int(offset) if registers[register] == 1 else 1, registers

    def run(self, seed: int = 0) -> int:
        instruction_fn: Dict[str, Any] = {
            'hlf': self.hlf,
            'tpl': self.tpl,
            'inc': self.inc,
            'jmp': self.jmp,
            'jie': self.jie,
            'jio': self.jio,
        }
        registers = {'a': seed, 'b': 0}
        address = 0
        while True:
            instruction, *parameters = split(r'[ ,]+', self.instructions[address])
            address_offset, registers = instruction_fn[instruction](registers, *parameters)
            address += address_offset
            if not 0 <= address < len(self.instructions):
                return registers['b']

    def solve1(self) -> int:
        return self.run()

    def solve2(self) -> int:
        return self.run(1)
