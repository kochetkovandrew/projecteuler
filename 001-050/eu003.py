from lib import Prime

test_number = 600851475143
factor = Prime()
decomp = factor.factorize(test_number)
print(decomp[-1])
