biggest = 0

for i in range(1, 9876):
    res = str(i)
    j = 2
    while len(res) < 9:
        res += str(i*j)
        j += 1
    if len(res) == 9:
        if sorted(res) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if int(res) > biggest:
                biggest = int(res)

print(biggest)
