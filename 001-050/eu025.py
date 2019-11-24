index = 2
prev = 1
curr = 1

while curr < 10**999:
    next = prev + curr
    prev = curr
    curr = next
    index += 1

print(index)
