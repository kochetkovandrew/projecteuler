class Factorize:
    primes = [2]

    # def __init__(self):
    #     self.primes = [2]

    def factorize(self, cand):
        test_number = cand
        decomp = []
        for prime in self.primes:
            if prime ** 2 > test_number:
                break
            while test_number % prime == 0:
                test_number //= prime
                decomp.append(prime)
        if self.primes[-1] == 2:
            test_prime = 3
        else:
            test_prime = self.primes[-1] + 2
        while self.primes[-1] ** 2 <= test_number:
            test_result = True
            for prime in self.primes:
                if prime ** 2 >= test_prime:
                    break
                if test_prime % prime == 0:
                    test_result = False
                    break
            if test_result:
                self.primes.append(test_prime)
                if test_number % test_prime == 0:
                    decomp.append(test_prime)
                    while test_number % test_prime == 0:
                        test_number = test_number // test_prime
            test_prime = test_prime + 2
        if test_number != 1:
            decomp.append(test_number)
        return decomp
