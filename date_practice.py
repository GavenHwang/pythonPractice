# -*- coding:utf-8 -*-
import calendar
import datetime


# 获取月份第一天和最后一天
def getMonthFirstDayAndLastDay(year=None, month=None):
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)
    print(firstDay, lastDay)


if __name__ == '__main__':
    s = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H:%M:%S")
    print(s)
    getMonthFirstDayAndLastDay()