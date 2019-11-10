f = open('eu013.txt', 'r')
sum = 0
lines = f.readlines()

for line in lines:
    sum += int(line)

print(str(sum)[0:10])
