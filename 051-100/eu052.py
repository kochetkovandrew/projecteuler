def to_list(num):
    check_num = num
    n_list = []
    while check_num > 0:
        n_list.append(check_num % 10)
        check_num //= 10
    return n_list


def check(num):
    # print(num)
    x1 = to_list(num)
    x2 = to_list(num * 2)
    x3 = to_list(num * 3)
    x4 = to_list(num * 4)
    x5 = to_list(num * 5)
    x6 = to_list(num * 6)
    x1.sort()
    x2.sort()
    x3.sort()
    x4.sort()
    x5.sort()
    x6.sort()
    if (x1 == x2) and (x1 == x3) and (x1 == x4) and (x1 == x5) and (x1 == x6):
        print(num)
        return True
    else:
        return False


def fill(digits, i, num):
    if i == 1:
        lim_d = 1
        lim_u = 1
    elif i == 2:
        lim_d = 0
        lim_u = 5
    else:
        lim_d = 0
        lim_u = 9
    j = lim_d
    while j <= lim_u:
        new_num = num * 10 + j
        if i == digits:
            res = check(new_num)
            if res:
                return True
        else:
            res = fill(digits, i + 1, new_num)
            if res:
                return True
        j += 1
    return False


digits = 1

res = False
while not res:
    res = fill(digits, 1, 0)
    if res:
        break
    digits += 1
