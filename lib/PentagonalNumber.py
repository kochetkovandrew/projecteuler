import math

class PentagonalNumber:
    numbers = [1]

    def next_number(self):
        position = len(self.numbers) + 1
        self.numbers.append((position * (3*position - 1)) // 2)

    def is_pentagonal(self, p):
        d = 24 * p + 1
        sqrtd = round(math.sqrt(d))
        if sqrtd**2 != d:
            return False
        else:
            return (1 + sqrtd) % 6 == 0
