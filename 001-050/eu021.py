import itertools
import functools
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
        sum += functools.reduce(lambda a, b: a * b, comb)
    divsums[i] = sum

res = 0

for i in range(2, border):
    if i < divsums[i] < border and i == divsums[divsums[i]]:
        res += i + divsums[i]

print(res)
