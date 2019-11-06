# import sys
from lib import Factorize

test_number = 600851475143
factor = Factorize()
decomp = factor.factorize(test_number)
print(decomp[-1])
