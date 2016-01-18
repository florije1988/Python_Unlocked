# -*- coding: utf-8 -*-
__author__ = 'florije'

import collections


def func():
    print("adf")


func()
func.__call__()
func.__class__.__call__(func)

print(func.__call__)


class C:
    def __call__(self):
        print("adf")


c = C()
c()

c.__call__()
c.__class__.__call__(c)
print(callable(lambda x: x + 1))
print(isinstance(lambda x: x + 1, collections.Callable))


class D:
    pass


class D1:
    def do(self, ):
        print("do run", self)


def doo(obj):
    print("doo run", obj)


d1 = D1()
d = D()

doo(d1)
doo(d)

d1.do()

D1.doo = doo
d1.doo()
D1.doo()
D1.do()
D1.do(d1)
D1.do(d)
d1.do.__func__(d)
