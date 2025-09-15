import itertools

f = open('p022_names.txt', 'r')
line = f.readlines()[0]
names = list(map(lambda x: x.strip('"'), line.split(',')))
names.sort()


def char_values(name):
    return map(lambda char: ord(char) - ord('A') + 1, name)


def char_sum(name):
    return sum(char_values(name))


ordered_sums = zip(map(lambda name: char_sum(name), names), itertools.count(1))
products = itertools.starmap(lambda i, j: i * j, ordered_sums)
print(sum(products))
