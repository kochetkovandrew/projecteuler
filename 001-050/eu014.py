lengths = [0]
max = 0
maxn = 0

for i in range(1, 1000000):
    cand = i
    cnt = 0
    while (cand != 1) and (cand >= i):
        if cand % 2 == 0:
            cand //= 2
        else:
            cand = 3 * cand + 1
        cnt += 1
    if cand != 1:
        cnt += lengths[cand]
    lengths.append(cnt)
    if cnt > max:
        max = cnt
        maxn = i

print(maxn)
