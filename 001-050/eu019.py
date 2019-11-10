year = 1900
month = 1
day_of_week = 1

def day_count(year, month):
    if month == 2:
        if year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

cnt = 0

while year <= 2000:
    if year >= 1901 and day_of_week == 0:
        cnt += 1
    day_of_week += day_count(year, month)
    day_of_week %= 7
    month += 1
    if month > 12:
        month = 1
        year += 1

print(cnt)
