from lib import Prime

prime = Prime()

i = 2
found = False
need_len = 4
factors = []

while not found:
    if len(factors) == need_len:
        factors = factors[1:]
    factors.append(prime.power_factorize(i))
    if len(factors) == need_len:
        local_found = True
        for j in range(0, need_len):
            if len(factors[j]) != need_len:
                local_found = False
                break
        if local_found:
            for j in range(0, need_len):
                for k in range(j+1, need_len):
                    for l in range(0, need_len):
                        if factors[j][l][0] == factors[k][l][0] and factors[j][l][1] == factors[k][l][1]:
                            local_found = False
        if local_found:
            prod = 1
            for fact in factors[0]:
                prod *= fact[0]**fact[1]
            print(prod)
            found = True
    i += 1
