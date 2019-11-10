pwr = 1000
digsum = 0
num = 2**pwr
while num > 0:
    digsum += num%10
    num //= 10
print(digsum)
