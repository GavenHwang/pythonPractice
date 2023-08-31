# -*- coding:utf-8 -*-
import calendar
import datetime


def get_month_first_day_and_last_day(year=datetime.date.today().year, month=datetime.date.today().month):
    """获取月份第一天和最后一天"""
    year, month = int(year), int(month)
    # 获取当月第一天的星期和当月的总天数
    first_day_week_day, month_range = calendar.monthrange(year, month)
    # 获取当月的第一天
    first_day = datetime.date(year=year, month=month, day=1)
    last_day = datetime.date(year=year, month=month, day=month_range)
    print(first_day, last_day)


def print_daily_work_date(year=datetime.date.today().year, month=datetime.date.today().month):
    first_day_week_day, month_range = calendar.monthrange(year, month)
    week_dir = {
        0: "周一",
        1: "周二",
        2: "周三",
        3: "周四",
        4: "周五",
        5: "周六",
        6: "周日",
    }
    for i in range(1, month_range + 1):
        t = datetime.date(year=year, month=month, day=i)
        print(t, week_dir.get(t.weekday()))


if __name__ == '__main__':
    now = datetime.datetime.now()
    print(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
    print(datetime.datetime.strftime(now.replace(hour=now.hour + 1, minute=0, second=0, microsecond=0),
                                     "%Y-%m-%d %H:%M:%S"))
    get_month_first_day_and_last_day()
    print_daily_work_date()
