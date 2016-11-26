def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_of_month(year, month):

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28


def next_day(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < days_of_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def is_before_date(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not is_before_date(year2, month2, day2, year1, month1, day1)
    days = 0
    while is_before_date(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1
    return days


def week_of_date(year, month):
    before = is_before_date(1990, 1, 1, year, month, days_of_month(year, month))
    if before:
        days = days_between_dates(1990, 1, 1, year, month, days_of_month(year, month)) + 1
        return days % 7
    else:
        days = days_between_dates(year, month, days_of_month(year, month), 1990, 1, 1) - 1
        return (0 - days) % 7

if __name__=='__main__':
    year = raw_input("year:")
    month = raw_input("month:")
    print week_of_date(int(year), int(month))
 
 
结果：
C:\Python27\python.exe D:/PycharmProjects/untitled/lesson3/1900_1_1.py
year:2003
month:12
3
 
Process finished with exit code 0