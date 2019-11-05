f1 = 1
f2 = 2
sum = 0
border = 4000000
while f2 < border:
    if f2 % 2 == 0:
        sum = sum + f2
    next_f = f1 + f2
    f1 = f2
    f2 = next_f
print(sum)
