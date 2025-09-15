from fractions import Fraction

lim = 999
longest_length = 0
longest_number = 0

for i in range(2, lim + 1):
    rational = Fraction(1, i)
    j = 1
    dec_parts = [0]
    rests = [1]
    found = False
    while rational != 0 and not found:
        dec_part = (rational / Fraction(1, 10 ** j)).__floor__()
        dec_parts.append(dec_part)
        rational -= Fraction(dec_part, 10 ** j)
        rests.append(rational * 10 ** j)
        for k in range(0, len(rests) - 1):
            if rests[k] == rests[-1]:
                length = len(rests) - k - 1
                if length > longest_length:
                    longest_length = length
                    longest_number = i
                found = True
                break
        j += 1

print(longest_number)
