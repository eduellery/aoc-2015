from functools import reduce


class SummedCombos:
    def __init__(self, seq, target_sum, max_len, shortest=False):
        self.seq = seq
        self.target_sum = target_sum
        self.max_len = max_len
        self.shortest = shortest

    def __iter__(self):
        return self.work(self.seq, [])

    @staticmethod
    def choice_rest(items):
        for i in range(len(items)):
            yield items[i], items[i + 1:]

    def work(self, remaining, so_far):
        if len(so_far) > self.max_len:
            return
        total = sum(so_far)
        if total == self.target_sum:
            if self.shortest:
                self.max_len = len(so_far)
            yield so_far
            return
        elif total > self.target_sum:
            return
        for choice, rest in SummedCombos.choice_rest(remaining):
            yield from self.work(rest, so_far + [choice])


class Day24:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers
        self.packages = sorted(self.numbers, reverse=True)
        self.sum_3 = sum(self.packages) // 3
        self.len_3 = len(self.packages) // 3
        self.sum_4 = sum(self.packages) // 4
        self.len_4 = len(self.packages) // 4

    @staticmethod
    def product(seq) -> int:
        return reduce(lambda a, b: int(a * b), seq, 1)

    def equal_3(self):
        min_qe = self.product(self.numbers)
        for g1 in SummedCombos(self.packages, self.sum_3, self.len_3, shortest=True):
            qe = self.product(g1)
            if qe > min_qe:
                continue
            min_qe = qe
            r = [p for p in self.packages if p not in g1]
            for g2 in SummedCombos(r, self.sum_3, self.len_3):
                answer = g1, g2, [p for p in r if p not in g2]
                yield answer
                break

    def equal_4(self):
        min_qe = self.product(self.numbers)
        for g1 in SummedCombos(self.packages, self.sum_4, self.len_4, shortest=True):
            qe = self.product(g1)
            if qe > min_qe:
                continue
            min_qe = qe
            r1 = [p for p in self.packages if p not in g1]
            for g2 in SummedCombos(r1, self.sum_4, self.len_4):
                r2 = [p for p in r1 if p not in g2]
                for g3 in SummedCombos(r2, self.sum_4, self.len_4):
                    answer = g1, g2, g3, [p for p in r2 if p not in g3]
                    yield answer
                    break
                break

    def solve1(self) -> int:
        return self.product(min(self.equal_3())[0])

    def solve2(self) -> int:
        return self.product(min(self.equal_4())[0])
