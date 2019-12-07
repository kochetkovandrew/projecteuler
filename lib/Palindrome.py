def check_pal(cand):
    cand_str = str(cand)
    cand_len = len(cand_str)
    res = True
    for i in range(0, cand_len):
        if cand_str[i] != cand_str[cand_len - i - 1]:
            res = False
            break
    return res
