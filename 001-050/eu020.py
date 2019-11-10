def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


def digsum(n):
    sum = 0
    cand = n
    while cand > 0:
        sum += cand % 10
        cand //= 10
    return sum


print(digsum(fact(100)))
