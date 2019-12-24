sum = 0
mod = 10000000000

for i in range(1, 1001):
    sum += pow(i, i, mod)

sum %= mod
print(sum)
