# -*- coding: utf-8 -*-
__author__ = 'florije'


def test_func(name):
    var = 10
    print(id(var))
    return name


if __name__ == '__main__':
    name = 'xiaoqigui'
    res = test_func(name)
    print(res)
