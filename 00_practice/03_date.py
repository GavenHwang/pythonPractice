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

def print_daily_work_date(year=datetime.date.today().year, month=datetime.date.today().month):
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    weekdir = {
        0: "周一",
        1: "周二",
        2: "周三",
        3: "周四",
        4: "周五",
        5: "周六",
        6: "周日",
    }
    for i in range(1, monthRange):
        t = datetime.date(year=year, month=month, day=i)
        print(t, weekdir.get(t.weekday()))


if __name__ == '__main__':
    # s = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H:%M:%S")
    # print(s)
    # getMonthFirstDayAndLastDay()
    print_daily_work_date()