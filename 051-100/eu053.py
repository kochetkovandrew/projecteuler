import math


def comb_count(n, r):
    list1 = [i for i in range(n - r + 1, n + 1)]
    list2 = [i for i in range(1, r + 1)]
    prod1 = 1
    prod2 = 1
    for i in range(0, len(list1)):
        prod1 *= list1[i]
        prod2 *= list2[i]
        gcd = math.gcd(prod1, prod2)
        prod1 //= gcd
        prod2 //= gcd
    return prod1


sum = 0
for i in range(23, 101):
    for j in range(1, (i // 2) + 1 + (i % 2)):
        if comb_count(i, j) > 1000000:
            sum += (i - (j - 1) * 2 - 1)
            break

print(sum)
