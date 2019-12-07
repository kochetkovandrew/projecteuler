from lib import check_pal

max = 0

for i in range(999, 9, -1):
    for j in range(999, i-1, -1):
        mult = i * j
        if check_pal(mult):
            if mult > max:
                max = mult
            break
        if mult < max:
            break

print(max)
