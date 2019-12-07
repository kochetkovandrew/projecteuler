from lib import Prime

truncatable_primes = []
prime = Prime()

def check_truncatable(cand):
    res = True
    tmp = cand
    while tmp > 0 and res:
        if not prime.is_prime(tmp):
            res = False
            break
        tmp //= 10
    tmp = cand % 10
    i = 1
    while tmp != cand and res:
        if not prime.is_prime(tmp):
            res = False
            break
        tmp += ((cand // 10**i) % 10) * 10**i
        i += 1
    return res

while len(truncatable_primes) < 11:
    if prime.primes[-1] < 10:
        prime.next_prime()
        continue
    if check_truncatable(prime.primes[-1]):
        truncatable_primes.append(prime.primes[-1])
    prime.next_prime()

print(sum(truncatable_primes))
