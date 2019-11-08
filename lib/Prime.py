class Prime:
    primes = [2]

    def next_prime(self):
        if self.primes[-1] == 2:
            test_prime = 3
        else:
            test_prime = self.primes[-1] + 2
        test_result = False
        while not test_result:
            test_result = True
            for prime in self.primes:
                if prime ** 2 > test_prime:
                    break
                if test_prime % prime == 0:
                    test_result = False
                    break
            if test_result:
                self.primes.append(test_prime)
            else:
                test_prime += 2

    def factorize(self, cand):
        test_number = cand
        decomp = []
        for prime in self.primes:
            if prime ** 2 > test_number:
                break
            while test_number % prime == 0:
                test_number //= prime
                decomp.append(prime)
        while self.primes[-1] ** 2 <= test_number:
            self.next_prime()
            while test_number % self.primes[-1] == 0:
                decomp.append(self.primes[-1])
                test_number = test_number // self.primes[-1]
        if test_number != 1:
            decomp.append(test_number)
        return decomp
