from lib import Prime

prime = Prime()

max_length = 0
max_a = 0
max_b = 0

while prime.next_prime() < 1000:
    pass

for b in prime.primes:
    if b > 1000:
        break
    for a in range(-999, 1000):
        n = 0
        while prime.is_prime(n ** 2 + a * n + b):
            n += 1
        if n > max_length:
            max_length = n
            max_a = a
            max_b = b

print(max_a * max_b)
