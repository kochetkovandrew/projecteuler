from lib import Factorize
max = 20
decomps = []
final_decomp = {}
factor = Factorize()

for i in range(2, max+1):
    decomp = factor.factorize(i)
    for num in set(decomp):
        cnt = decomp.count(num)
        if not(num in final_decomp) or (final_decomp[num] < cnt):
            final_decomp[num] = cnt

res = 1
for num, pwr in final_decomp.items():
    res *= num**pwr

print(res)
