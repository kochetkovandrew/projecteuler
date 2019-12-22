from lib import Prime

prime = Prime()

found = False
i = 3

while not found:
    if not prime.is_prime(i):
        while prime.primes[-1] < i:
            prime.next_prime()
        j = 1
        local_found = False
        while 2*(j**2) < i:
            if prime.is_prime(i - 2*(j**2)):
                local_found = True
                break
            j += 1
        if not local_found:
            print(i)
            found = True
    i += 2
