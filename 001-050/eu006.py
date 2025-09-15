max = 100

sum = 0
sumsq = 0
for i in range(1, max + 1):
    sum += i
    sumsq += i ** 2

print(sum ** 2 - sumsq)
