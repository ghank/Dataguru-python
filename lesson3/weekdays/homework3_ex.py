#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:
@file: homework4_ex.py
@time: 2016/10/23 11:34
"""

#非闰年 每月天数
monthdays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
#非闰年与闰年对应的天数
yeardays = {0:365, 1:366}

#计算是否是闰年
def leapYear(year):
    assert year>0, u"输入年份必须大于零的整数"
    if (year%4==0 and year%100!=0) or (year%400==0):
        return 1
    return 0

#计算星期几
def Weekday(days):
    # assert type(days) == type(int), u"输入天数必须大于零的整数"
    # 星期
    week = {-6: u'星期一', -5: u'星期二', -4: u'星期三', -3: u'星期四', -2: u'星期五', -1: u'星期六', 0: u'星期日', \
            1: u'星期一', 2: u'星期二', 3: u'星期三', 4: u'星期四', 5: u'星期五', 6: u'星期六'}
    return week[days%7]

#计算与1990年1月1日相距的时间
def sumWeekday(year, month):
    assert year>0 and (month>=1 and month<=12), u"输入年月份必须大于零的整数"
    days = 0
    if year >= 1990:
        for elem in range(1990, year):
            days += yeardays[leapYear(elem)]
        for elem in range(1, month+1):
            if leapYear(year)==1 and elem ==2:
                days += monthdays[elem] + 1
            else:
                days += monthdays[elem]
    else:
        for elem in range(year, 1990):
            days -= yeardays[leapYear(elem)]
        for elem in range(1, month+1):
            if leapYear(year)==1 and elem ==2:
                days += monthdays[elem] + 1
            else:
                days += monthdays[elem]
    return Weekday(days)

if __name__ == "__main__":
    year = input("请输入年份：")
    month = input("请输入月份：")
    print sumWeekday(year, month)






