def is_leap(year):
    leap = False

    yearDividedFour = float(year/4)
    if (yearDividedFour).is_integer():
        if (year/100).is_integer():
            if (year/400).is_integer():
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))
