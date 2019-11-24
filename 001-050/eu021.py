from lib import Prime

factor = Prime()

border = 10000
divsums = {}

for i in range(2, border):
    divsums[i] = sum(factor.proper_divisors(i))

res = 0

for i in range(2, border):
    if i < divsums[i] < border and i == divsums[divsums[i]]:
        res += i + divsums[i]

print(res)
