"""
Module for calculating hexagonal numbers.
"""


class HexagonalNumber:
    """Class to generate and store hexagonal numbers."""
    numbers = [1]

    def next_number(self):
        """Generate the next hexagonal number and add it to the list."""
        position = len(self.numbers) + 1
        self.numbers.append(position * (2 * position - 1))
