from hashlib import md5


class Day04:
    def __init__(self, secret: str):
        self.secret = secret

    def calculate_hash(self, zeros: int, limit: int = 10 ** 7) -> int:
        for i in range(limit):
            m = md5((self.secret + str(i)).encode('utf-8'))
            if m.hexdigest().startswith('0' * zeros):
                return i
        return -1

    def solve1(self) -> int:
        return self.calculate_hash(5)

    def solve2(self) -> int:
        return self.calculate_hash(6)
