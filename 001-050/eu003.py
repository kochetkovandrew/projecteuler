test_number = 600851475143

primes = [2]
decomp = []
test_prime = 3
while primes[-1]**2 <= test_number:
    test_result = True
    for prime in primes:
        if prime**2 >= test_prime:
            break
        if test_prime%prime == 0:
            test_result = False
            break
    if test_result:
        primes.append(test_prime)
        if test_number % test_prime == 0:
            decomp.append(test_prime)
            while test_number % test_prime == 0:
                test_number = test_number // test_prime
    test_prime = test_prime + 2
if test_number != 1:
    decomp.append(test_number)

print(decomp[-1])
