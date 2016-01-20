# -*- coding: utf-8 -*-
__author__ = 'florije'

"""
编写程序，判断给定的某个年份是否是闰年。
闰年的判断规则如下：
（1）若某个年份能被4整除但不能被100整除，则是闰年。
（2）若某个年份能被400整除，则也是闰年。

"""

if __name__ == '__main__':
    year = int(input('Please input the year!(year>0):'))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Year {year} is leap.'.format(year=year))
    else:
        print('Year {year} is not leap.'.format(year=year))
