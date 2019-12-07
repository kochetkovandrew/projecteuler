facts = {}

fact = 1
facts[0] = 1
for i in range(1, 10):
    fact *= i
    facts[i] = fact

def sumfacts(cand):
    summ = 0
    while cand > 0:
        summ += facts[cand % 10]
        cand //= 10
    return summ

summ = 0

for i in range(10, 2540161):
    if i == sumfacts(i):
        summ += i

print(summ)
