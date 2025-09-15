"""
Module for generating and checking pentagonal numbers.
"""
import math


class PentagonalNumber:
    numbers = [1]

    def next_number(self):
        """Generate the next pentagonal number and add it to the list."""
        position = len(self.numbers) + 1
        self.numbers.append((position * (3 * position - 1)) // 2)

    def is_pentagonal(self, p):
        """Check if a number is pentagonal using the inverse formula."""
        d = 24 * p + 1
        sqrtd = round(math.sqrt(d))
        if sqrtd ** 2 != d:
            return False
        else:
            return (1 + sqrtd) % 6 == 0
