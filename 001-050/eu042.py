from lib import TriangleNumber

triangle_number = TriangleNumber()

f = open('p042_words.txt', 'r')
line = f.readlines()[0]
words = list(map(lambda x: x.strip('"'), line.split(',')))

count = 0


def char_values(word):
    return map(lambda char: ord(char) - ord('A') + 1, word)


def char_sum(word):
    return sum(char_values(word))


for word in words:
    chsum = char_sum(word)
    while triangle_number.triangle_numbers[-1] < chsum:
        triangle_number.next_number()
    if chsum in triangle_number.triangle_numbers:
        count += 1

print(count)
