words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
         20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def pronounce(i):
    if i in words.keys():
        return words[i]
    elif i < 100:
        str = words[i - (i % 10)]
        if i % 10 != 0:
            str += '-' + words[i % 10]
        return str
    elif i < 1000:
        str = words[i // 100] + ' hundred'
        if i % 100 != 0:
            str += ' and '
            str += pronounce(i % 100)
        return str
    else:
        str = pronounce(i // 1000) + ' thousand'
        if i % 1000 != 0:
            str += ' ' + pronounce(i % 1000)
        return str


sumlen = 0

for i in range(1, 1001):
    sumlen += len(pronounce(i).replace(' ', '').replace('-', ''))

print(sumlen)
