from lib import Prime

border = 2000000

prime = Prime()
while prime.primes[-1] < border:
    prime.next_prime()

sum = 0
for i in prime.primes:
    if i < border:
        sum += i
    else:
        break

print(sum)
