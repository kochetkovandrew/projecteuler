from lib import Prime

prime = Prime()
lim = 1000000

max_len = 0
max_sum = 0

while prime.primes[-1] < lim:
    prime.next_prime()

for i in range(0, len(prime.primes) - 1):
    sum = prime.primes[i]
    for j in range(i + 1, len(prime.primes) - 1):
        sum += prime.primes[j]
        if sum >= lim:
            break
        if sum in prime.primes:
            if max_len < (j - i + 1):
                max_len = j - i + 1
                max_sum = sum

print(max_len)
print(max_sum)
