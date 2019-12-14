class TriangleNumber:
    triangle_numbers = [1]

    def next_number(self):
        position = len(self.triangle_numbers) + 1
        self.triangle_numbers.append((position * (position + 1)) // 2)

