import itertools
from lib import Prime

factor = Prime()

border = 10000
divsums = {}

for i in range(2, border):
    fact = factor.factorize(i)
    combies = []
    for j in range(1, len(fact)):
        combies += list(itertools.combinations(fact, j))
    combies = list(dict.fromkeys(combies))
    sum = 1
    for comb in combies:
        prod = 1
        for num in comb:
            prod *= num
        sum += prod
    divsums[i] = sum

res = 0

for i in range(2, border):
    if divsums[i] > i and divsums[i] < border and i == divsums[divsums[i]]:
        res += i
        res += divsums[i]

print(res)
