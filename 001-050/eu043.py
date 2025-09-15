def generate_pandigital(digits, number):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    summ = 0
    for i in digits:
        if len(number) == 0 and i == 0:
            continue
        new_number = list(number)
        new_number.append(i)
        new_digits = list(set(digits) - set([i]))
        if len(new_number) >= 4:
            cand = int(''.join(list(map(lambda x: str(x), new_number[len(new_number) - 3:len(new_number)]))))
            if cand % divisors[len(new_number) - 4] != 0:
                continue
        if len(new_number) == 10:
            num = int(''.join(list(map(lambda x: str(x), new_number))))
            summ += num
        else:
            summ += generate_pandigital(new_digits, new_number)
    return summ


print(generate_pandigital(list(range(0, 10)), []))
