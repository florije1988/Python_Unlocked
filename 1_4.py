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
