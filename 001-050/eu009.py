res = 0
for a in range(1, 998):
    for b in range(a+1, 999-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            res = a*b*c
            break
    if res > 0:
        break
print(res)
