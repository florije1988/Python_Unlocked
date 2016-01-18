# -*- coding: utf-8 -*-
__author__ = 'florije'

k = []
print(k.__class__)
type(k)


class M:
    def __init__(self, d):
        self.d = d

    def square(self):
        return self.d * self.d


class N:
    def __init__(self, d):
        self.d = d

    def cube(self):
        return self.d * self.d * self.d


m = M(4)
print(type(m))

print(m.square())
m.__class__ = N
print(m.cube())  # 因为是动态的更改类型，所以这里找不到。
print(type(m))
