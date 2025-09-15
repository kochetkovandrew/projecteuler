f = open('eu011.txt', 'r')
arr = []
max_prod = 0
prod_cnt = 4
lines = f.readlines()

for line in lines:
    nums = list(map(lambda elem: int(elem), line.split()))
    arr.append(nums)
length = len(arr[0])

for i in range(0, length):
    for j in range(0, length):
        if j + prod_cnt <= length:
            prod = 1
            for k in range(0, prod_cnt):
                prod *= arr[i][j + k]
            if prod > max_prod:
                max_prod = prod
        if i + prod_cnt <= length:
            prod = 1
            for k in range(0, prod_cnt):
                prod *= arr[i + k][j]
            if prod > max_prod:
                max_prod = prod
        if i + prod_cnt <= length and j + prod_cnt <= length:
            prod = 1
            for k in range(0, prod_cnt):
                prod *= arr[i + k][j + k]
            if prod > max_prod:
                max_prod = prod
        if i + prod_cnt <= length and j - prod_cnt >= 0:
            prod = 1
            for k in range(0, prod_cnt):
                prod *= arr[i + k][j - k]
            if prod > max_prod:
                max_prod = prod

print(max_prod)
