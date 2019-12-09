from lib import Prime

def check_pandigital(cand):
    arr = sorted(str(cand))
    i = 1
    res = True
    while i < 10 and i < len(arr) + 1:
        if int(arr[i-1]) != i:
            res = False
            break
        i += 1
    return res

prime = Prime()

biggest = 0

while prime.primes[-1] <= 987654321:
    if check_pandigital(prime.primes[-1]):
        biggest = prime.primes[-1]
    prime.next_prime()

print(biggest)
