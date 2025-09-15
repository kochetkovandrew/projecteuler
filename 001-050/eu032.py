def digits(a):
    list = []
    while a > 0:
        list.append(a % 10)
        a //= 10
    return list


def checkprod(a, b):
    return sorted(digits(a) + digits(b) + digits(a * b))


prods = []

for i in range(1, 99):
    j = i + 1
    while True:
        res = checkprod(i, j)
        if res == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            prods.append(i * j)
        if len(res) > 9:
            break
        j += 1

print(sum(dict.fromkeys(prods)))
