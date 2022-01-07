from re import sub, findall
from typing import List


class Day11:
    def __init__(self, seed: str):
        self.passwords: List[str] = [''] * 2
        self.passwords[0] = self.next_password(seed)
        self.passwords[1] = self.next_password(self.passwords[0])

    @staticmethod
    def next_password(password):
        while True:
            password = sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1)) + 1) + len(x.group(2)) * "a", password)
            if ("i" in password or "o" in password or "l" in password) or \
                    (len(findall(r'([a-z])\1', password)) < 2) or \
                    (len([1 for x, y, z in zip(password, password[1:], password[2:])
                          if ord(z) - ord(y) == 1 and ord(y) - ord(x) == 1]) == 0):
                continue
            return password

    def solve1(self) -> str:
        return self.passwords[0]

    def solve2(self) -> str:
        return self.passwords[1]
