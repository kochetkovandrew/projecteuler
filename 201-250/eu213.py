"""
A 30x30 grid of squares contains 900 fleas, initially one flea per square.
When a bell is rung, each flea jumps to an adjacent square at random
(usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell?
Give your answer rounded to six decimal places.
"""

# Each layer corresponds to one flea
# Each layer is a 30x30 grid
source_field = [[[0 for _ in range(30)] for _ in range(30)] for _ in range(900)]

# Initially one flea per square
# There are 900 fleas, each starts at a different square in its own layer
for i in range(30):
    for j in range(30):
        source_field[i * 30 + j][i][j] = 1.0


def step():
    """
    One step of all fleas
    Each flea jumps to an adjacent square at random
    4 possibilities, except for fleas on the edge of the grid or at the corners
    900 fleas, each in its own layer
    30x30 grid
    """
    for flea in range(900):
        target_field = [[0 for _ in range(30)] for _ in range(30)]
        for i in range(30):
            for j in range(30):
                if source_field[flea][i][j] > 0:
                    cnt = 0
                    if i > 0:
                        cnt += 1
                    if i < 29:
                        cnt += 1
                    if j > 0:
                        cnt += 1
                    if j < 29:
                        cnt += 1

                    if i > 0:
                        target_field[i - 1][j] += source_field[flea][i][j] / cnt
                    if i < 29:
                        target_field[i + 1][j] += source_field[flea][i][j] / cnt
                    if j > 0:
                        target_field[i][j - 1] += source_field[flea][i][j] / cnt
                    if j < 29:
                        target_field[i][j + 1] += source_field[flea][i][j] / cnt

        for i in range(30):
            for j in range(30):
                source_field[flea][i][j] = target_field[i][j]


for _ in range(50):
    step()

res = 0
for i in range(30):
    for j in range(30):
        product = 1
        for flea in range(900):
            product *= (1 - source_field[flea][i][j])
        res += product  # prob of being empty

print(f"{res:.6f}")
