f = open('eu008.txt', 'r')
arr = []
numbers_count = 13
max_prod = 0
lines = f.readlines()
for line in lines:
    for ch in line.rstrip():
        arr.append(ord(ch) - ord('0'))
for i in range(0, len(arr) - numbers_count + 1):
    res = 1
    for j in range(0, numbers_count):
        res *= arr[i+j]
    if res > max_prod:
        max_prod = res
print(max_prod)
