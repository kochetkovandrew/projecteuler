from lib import Prime

factor = Prime()
border = 28123
abundants = []

for i in range(2, border+1):
    proper_divisors = factor.proper_divisors(i)
    if sum(proper_divisors) > i:
        abundants.append(i)

abundant_sums = {i: False for i in range(1, border+1)}

for cand1 in abundants:
    for cand2 in abundants:
        if cand1 + cand2 <= border:
            abundant_sums[cand1 + cand2] = True

result = 0
for key, value in abundant_sums.items():
    if not value:
        result += key

print(result)
