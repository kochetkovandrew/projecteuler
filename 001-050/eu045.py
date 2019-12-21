from lib import TriangleNumber
from lib import PentagonalNumber
from lib import HexagonalNumber

found = False

triangle = TriangleNumber()
pentagonal = PentagonalNumber()
hexagonal = HexagonalNumber()

while not found:
    while triangle.triangle_numbers[-1] < hexagonal.numbers[-1]:
        triangle.next_number()
    while pentagonal.numbers[-1] < hexagonal.numbers[-1]:
        pentagonal.next_number()
    if hexagonal.numbers[-1] == pentagonal.numbers[-1] and hexagonal.numbers[-1] == triangle.triangle_numbers[-1]:
        if hexagonal.numbers[-1] > 40755:
            print(hexagonal.numbers[-1])
            found = True
        else:
            hexagonal.next_number()
    else:
        hexagonal.next_number()
