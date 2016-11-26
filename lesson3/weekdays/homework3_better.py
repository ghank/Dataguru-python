#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: homework4_better.py
@time: 2016/10/23 12:50
"""

#计算是否是闰年
def leapYear(year):
    assert year>0, u"输入年份必须大于零的整数"
    if (year%4==0 and year%100!=0) or (year%400==0):
        return 1
    return 0

#判定日期的前后顺序
#True表示year1-month1-day1提前于year2-month2-day2
def isBeforeDate(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            return day1 < day2
    return False


# 计算每月的天数
def daysOfMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if leapYear(year):
            return 29
        else:
            return 28

# 计算出两个日期之间的天数（更具有通用性）
#year2-month2-day2 - year1-month1-day1
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not isBeforeDate(year2, month2, day2, year1, month1, day1)
    yeardays, monthdays1, monthdays2, days = 0, 0, 0, 0
    #计算年之间的天数
    for elem in range(year1, year2):
        if leapYear(elem):
            yeardays += 366
        else:
            yeardays += 365
    #计算1月至month之前的天数
    if month1 > 1:
        for elem in range(1,month1):
            monthdays1 += daysOfMonth(year1, elem)
    if month2 > 1:
        for elem in range(1, month2):
            monthdays2 += daysOfMonth(year2, elem)

    days = yeardays + (monthdays2-monthdays1) + (day2-day1)
    return days

#计算星期几
def weekDay(days):
    #assert days >= 0, u"输入天数必须大于零的整数"
    week = {-6: u'星期一', -5: u'星期二', -4: u'星期三', -3: u'星期四', -2: u'星期五', -1: u'星期六', \
            0: u'星期日', 1: u'星期一', 2: u'星期二', 3: u'星期三', 4: u'星期四', 5: u'星期五', 6: u'星期六'}
    return week[days%7]


#功能函数
def sumWeekday(year, month):
    #计算除这个月有多少天
    day = daysOfMonth(year, month)
    if isBeforeDate(1990, 1, 1, year, month, day):
        days = daysBetweenDates(1990, 1, 1, year, month, day) + 1
        return weekDay(days)
    else:
        days = daysBetweenDates(year, month, day, 1990, 1, 1) - 1
        return weekDay(-days)


if __name__ == "__main__":
    year = input("请输入年份：")
    month = input("请输入月份：")
    print sumWeekday(year, month)

