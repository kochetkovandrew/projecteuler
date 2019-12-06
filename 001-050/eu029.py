lim = 100

list = []

for a in range(2, lim+1):
    for b in range(2, lim+1):
        list.append(a**b)

print(len(dict.fromkeys(list)))
