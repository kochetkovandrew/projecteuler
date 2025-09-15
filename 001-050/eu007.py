from lib import Prime

num = 10001
prime = Prime()
while len(prime.primes) < num:
    prime.next_prime()

print(prime.primes[num - 1])
