from lib import check_pal

summ = 0

for i in range(1, 1000000):
    if check_pal('{0:b}'.format(i)) and check_pal('{0:d}'.format(i)):
        summ += i

print(summ)
