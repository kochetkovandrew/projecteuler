import itertools

def permutation_number(permutation):
    plist = list(permutation)
    result = 0
    for i in range(0, 10):
        result += plist[9-i] * 10**i
    return result

mapped_permutations = map(lambda permutation: permutation_number(permutation),
               itertools.permutations(range(0, 10), 10))
listed_permutations = list(mapped_permutations)
listed_permutations.sort()
print(str(listed_permutations[999999]).zfill(10))
