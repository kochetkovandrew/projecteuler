from lib import PentagonalNumber

min_diff = None
pentagon = PentagonalNumber()

while min_diff is None or (pentagon.numbers[-1] - pentagon.numbers[-2] < min_diff):
    pentagon.next_number()
    for i in range(-2, -len(pentagon.numbers), -1):
        if pentagon.numbers[i] * 2 < pentagon.numbers[-1]:
            break
        diff1 = pentagon.numbers[-1] - pentagon.numbers[i]
        summ1 = pentagon.numbers[-1] + pentagon.numbers[i]
        diff2 = pentagon.numbers[i]
        summ2 = pentagon.numbers[-1] + diff1
        if (min_diff is None or diff1 < min_diff) and pentagon.is_pentagonal(diff1) and pentagon.is_pentagonal(summ1):
            min_diff = diff1
        if ((min_diff is None or diff2 < min_diff) and pentagon.is_pentagonal(diff2) and
                pentagon.is_pentagonal(summ2) and pentagon.is_pentagonal(diff1)):
            min_diff = diff2
        if min_diff is not None and diff1 > min_diff:
            break

print(min_diff)
