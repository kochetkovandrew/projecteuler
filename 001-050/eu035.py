from lib import Prime

lim = 1000000
prime = Prime()


def circulars(n):
    digcnt = 0
    tmp = n
    res = []
    while tmp > 0:
        digcnt += 1
        tmp //= 10
    tmp = n
    for i in range(0, digcnt):
        res.append(tmp)
        dig = tmp % 10
        tmp //= 10
        tmp += dig * 10 ** (digcnt - 1)
    return res


while prime.primes[-1] < lim:
    prime.next_prime()

cnt = 0

for i in prime.primes:
    if i > lim:
        break
    circs = circulars(i)
    res = True
    for cand in circs:
        if cand not in prime.primes:
            res = False
            break
    if res:
        cnt += 1

print(cnt)
