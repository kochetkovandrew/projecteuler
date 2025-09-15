"""Prime number utilities."""
import itertools
import functools


class Prime:
    """Class for generating and working with prime numbers."""
    primes = [2]

    def next_prime(self):
        """Generate the next prime number and add it to the list."""
        # Start testing from the next odd number after the last prime
        if self.primes[-1] == 2:
            test_prime = 3
        else:
            test_prime = self.primes[-1] + 2
        test_result = False
        # Continue testing until a prime is found
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
                return self.primes[-1]
            else:
                test_prime += 2

    def factorize(self, cand):
        """Return the prime factorization of a candidate number as a list."""
        test_number = cand
        decomp = []
        for prime in self.primes:
            if prime ** 2 > test_number:
                break
            while test_number % prime == 0:
                test_number //= prime
                decomp.append(prime)
        # If the last prime squared is less than or equal to the test number, generate more primes
        while self.primes[-1] ** 2 <= test_number:
            self.next_prime()
            while test_number % self.primes[-1] == 0:
                decomp.append(self.primes[-1])
                test_number = test_number // self.primes[-1]
        if test_number != 1:
            decomp.append(test_number)
        return decomp

    def is_prime(self, cand):
        """Check if a candidate number is prime."""
        if cand < 2:
            return False
        decomp = self.factorize(cand)
        return len(decomp) == 1

    def power_factorize(self, cand):
        """Return the prime factorization of a candidate number as a list of [prime, power]."""
        decomp = self.factorize(cand)
        uniq_decomp = list(dict.fromkeys(decomp))
        return list(map(lambda x: [x, decomp.count(x)], uniq_decomp))

    def sigma_zero(self, cand):
        """
        Return the number of divisors of a candidate number.
        Example: 28 -> 6 (1, 2, 4, 7, 14, 28)
        """
        decomp = self.power_factorize(cand)
        prod = 1
        for x in decomp:
            prod *= (x[1] + 1)
        return prod

    def proper_divisors(self, cand):
        """
        Return a list of proper divisors of a candidate number.
        Example: 28 -> [1, 2, 4, 7, 14]
        """
        decomp = self.factorize(cand)
        combinations = []
        for j in range(1, len(decomp)):
            combinations += list(itertools.combinations(decomp, j))
        combinations = list(dict.fromkeys(combinations))
        result = [1]
        if len(combinations) > 0:
            result += map(lambda combination: functools.reduce(lambda a, b: a * b, combination), combinations)
        return result
