from fractions import Fraction

res = 1

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i*10 + j >= j*10 + k:
                continue
            if Fraction(i*10 + j, j*10 + k) == Fraction(i, k):
                res *= Fraction(i*10 + j, j*10 + k)

print(res.denominator)
