# encoding: UTF-8
def getWeekDay(year,month,day):
# print year,month,day
# 计算星期几的公式. 0-星期日；1-星期一；2-星期二；3-星期三；4-星期
四；5-星期五；6-星期六
iD = day
if(month == 1 or month ==2):
iM = month + 12
iY = year - 1
else:
iM = month
iY = year
return (iD + 1 + 2 * iM + 3 * (iM + 1) / 5 + iY + iY / 4 - iY /
100 + iY / 400) % 7
def isLeapYear(year):
return (year%4 == 0 and year%100 <> 0) or (year%400 == 0)
def getLastDay(year,month):
if(month in (1,3,5,7,8,10,12)):
return 31
# 判断 year 是否闰年
elif (month == 2):
if(isLeapYear(year)):
return 29
else:
return 28
else:
return 30
def getWeekDayOfYM(year,month):
day = getLastDay(year, month)
if ((year >= 0 and year <= 9999) and (month >= 1 and month <= 1
2)):
return ["success", getWeekDay(year, month, day)]
else:
return ["fail", "Please check the input value"]
