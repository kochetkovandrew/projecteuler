from lib import Prime
from itertools import permutations
from itertools import combinations

prime = Prime()

solutions = []


def check_pal(cand):
    digits = []
    primes = []
    while cand > 0:
        digits.append(cand % 10)
        cand //= 10
    for i in permutations(digits):
        new_cand = i[0] * 1000 + i[1] * 100 + i[2] * 10 + i[3]
        if new_cand >= 1000 and (new_cand in prime.primes):
            primes.append(new_cand)
    if len(primes) >= 3:
        for chunk in combinations(primes, 3):
            sorted = list(chunk)
            sorted.sort()
            if sorted[2] != sorted[1] and sorted[1] != sorted[0]:
                if sorted[2] - sorted[1] == sorted[1] - sorted[0]:
                    result = str(sorted[0]) + str(sorted[1]) + str(sorted[2])
                    if (not (result in solutions)) and (sorted[0] != 1487):
                        solutions.append(result)


while prime.primes[-1] < 10000:
    prime.next_prime()

for i in range(0, len(prime.primes) - 1):
    if prime.primes[i] >= 1000 and prime.primes[i] < 10000:
        check_pal(prime.primes[i])

print(solutions[0])
