"""
输入某年某月某日，
判断这一天是这一年的第几天？
"""

import datetime


def fun():
    year = int(input("请输入年份："))

    month = int(input("请输入月份："))

    day = int(input("请输入天："))

    date1 = datetime.date(year=int(year), month=int(month), day=int(day))

    date2 = datetime.date(year=int(year), month=1, day=1)

    return (date1 - date2).days + 1


if __name__ == '__main__':
    print(fun())
