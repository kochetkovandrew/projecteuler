max = 0

def check_pal(cand):
    cand_str = str(cand)
    cand_len = len(cand_str)
    res = True
    for i in range(0, cand_len):
        if cand_str[i] != cand_str[cand_len - i - 1]:
            res = False
            break
    return res

for i in range(999, 9, -1):
    for j in range(999, i-1, -1):
        mult = i * j
        if check_pal(mult):
            if mult > max:
                max = mult
            break
        if mult < max:
            break

print(max)
