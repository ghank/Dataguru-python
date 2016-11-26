1. 编写函数实现功能
#!/usr/bin/python
# encoding: utf-8 | #-*-coding:utf8-*- | coding:utf8


"""
@author: kenny
@file: task3_1.py
@time: 2016/10/23 19:11
"""

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0)

def days_of_month(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28

def next_day(year, month, day):
    if day < days_of_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

#Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False.
def is_before_date(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def days_between_dates(year1, month1, day1, year2, month2, day2):
    assert not is_before_date(year2, month2, day2, year1, month1, day1)
    days = 0
    while is_before_date(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1
    # print "A total of ",days," days from 1900/1/1."
    return days

def get_day_of_week(year,month):

    before = is_before_date(1900, 1, 1, year, month, days_of_month(year, month))
    if before:
        days = days_between_dates(1900, 1, 1, year, month, days_of_month(year, month)) + 1
        return days % 7
    else:
        days = days_between_dates(year, month, days_of_month(year, month), 1900, 1, 1) - 1
        return (0 - days) % 7

if __name__=='__main__':
    year = int(raw_input('Enter the year of the integer: '))
    month = int(raw_input('Enter the month of the integer:'))

    if month > 12 or month < 1:
        print "Input the month [",month,"] is invalid."
        exit()

    # if is_leap_year(year):
    #     print "This year [",year,"] is leap year!"
    # else:
    #     print "This year [",year,"] is not leap year!"

    # print year,"/",month,"last day:",days
    print get_day_of_week(int(year), int(month))

Result：
-------------
C:\Python\Anaconda2\python.exe C:/Python/PycharmProjects/learnpython/lession3/task3_1.py
Enter the year of the integer: 1984
Enter the month of the integer:10
3


Process finished with exit code 0

2、编写测试用例
import unittest
from lession3.task3_1 import get_day_of_week

class MyTestCase(unittest.TestCase):
    def test_get_week(self):
        year=1984
        month=11
        week=get_day_of_week(year,month)
        self.assertEqual(week, 5, "test ascending order failed")

if __name__ == '__main__':
    unittest.main()
Result:
------------------------
C:\Python\Anaconda2\python.exe "C:\Python\JetBrains\PyCharm Community Edition 2016.2.3\helpers\pycharm\noserunner.py" C:\Python\PycharmProjects\learnpython\unit_test\unit_task3_1_week.py
Testing started at 22:14 ...