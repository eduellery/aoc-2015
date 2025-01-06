from re import findall


class Day07:
    def __init__(self, instructions: list[str]):
        self.calc = dict()
        for line in instructions:
            instruction = findall(r'(.*)\s->\s(\w*)', line)
            for ops, register in instruction:
                self.calc[register] = ops.strip().split(' ')

    def calculate(self, register: str, results: dict[str, int]) -> int:
        try:
            return int(register)
        except ValueError:
            pass

        if register not in results:
            ops = self.calc[register]
            if len(ops) == 1:
                res = self.calculate(ops[0], results)
            else:
                op = ops[-2]
                if op == 'AND':
                    res = self.calculate(ops[0], results) & self.calculate(ops[2], results)
                elif op == 'OR':
                    res = self.calculate(ops[0], results) | self.calculate(ops[2], results)
                elif op == 'NOT':
                    res = ~self.calculate(ops[1], results) & 0xffff
                elif op == 'RSHIFT':
                    res = self.calculate(ops[0], results) >> self.calculate(ops[2], results)
                else: # op == 'LSHIFT'
                    res = self.calculate(ops[0], results) << self.calculate(ops[2], results)
            results[register] = res
        return results[register]

    def solve1(self) -> int:
        return self.calculate('a', dict())

    def solve2(self) -> int:
        result = dict()
        result['b'] = self.calculate('a', dict())
        return self.calculate('a', result)
