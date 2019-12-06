lim = 413343

def check_power(cand):
    summ = 0
    check = cand
    while check > 0:
        digit = check % 10
        summ += digit**5
        check //= 10
    return cand == summ

summ = 0

for i in range(10, lim+1):
    if check_power(i):
        summ += i

print(summ)
