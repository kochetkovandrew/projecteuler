import math

class HexagonalNumber:
    numbers = [1]

    def next_number(self):
        position = len(self.numbers) + 1
        self.numbers.append(position * (2*position - 1))
