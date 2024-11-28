from lib import check_pal

cnt = 0
for cand in range(1, 10000):
    found = False
    next_cand = cand
    for i in range(0, 50):
        next_cand = next_cand + int(str(next_cand)[::-1])
        if check_pal(next_cand):
            found = True
            break
    if not found:
        cnt += 1

print(cnt)

