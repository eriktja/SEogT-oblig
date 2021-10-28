def is_four_hundred(year):
    return year % 400


def is_one_hundred(year):
    if year % 100 == 0:
        return True
    else: 
        return False


def is_leap_year(year):
    y = is_four_hundred(year)
    if y == 0:
        return True
    elif is_one_hundred(y):
        return False
    elif y % 4 == 0:
        return True
    else:
        return False
