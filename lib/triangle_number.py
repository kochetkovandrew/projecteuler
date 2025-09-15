"""Module for generating triangle numbers."""


class TriangleNumber:
    """Class for generating and storing triangle numbers."""
    triangle_numbers = [1]

    def next_number(self):
        """Generate the next triangle number and add it to the list."""
        position = len(self.triangle_numbers) + 1
        self.triangle_numbers.append((position * (position + 1)) // 2)
