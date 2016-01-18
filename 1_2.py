# -*- coding: utf-8 -*-
__author__ = 'florije'


class C:
    def __init__(self, arg1, arg2):
        self.str = arg1
        self.lst = arg2


iC = C("arun", [1, 2])
print(iC.str)
print(iC.lst)
iC.lst.append(4)
print(iC.lst)
