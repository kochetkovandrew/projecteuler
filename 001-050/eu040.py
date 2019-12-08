position = 0
i = 1
next_position = 1
prod = 1

while next_position <= 1000000:
    while position < next_position:
        str_i = str(i)
        if position + len(str_i) >= next_position:
            prod *= int(str_i[next_position - position - 1])
        i += 1
        position += len(str_i)
    next_position *= 10

print(prod)
