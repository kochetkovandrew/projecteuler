nominals = [1, 2, 5, 10, 20, 50, 100, 200]

nominals.sort(reverse=True)

def step(summ, nominals):
    if summ == 0:
        return 1
    newnom = nominals
    cnt = 0
    while len(newnom) > 0:
        if newnom[0] <= summ:
            cnt += step(summ-newnom[0], newnom)
        newnom = newnom[1:]
    return cnt

print(step(200, nominals))
