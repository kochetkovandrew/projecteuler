summ = 1
last = 1
step = 2

size = 1001

for i in range(0, size // 2):
    summ += last*4 + step*10
    last += step*4
    step += 2

print(summ)
