# -*- coding: utf-8 -*-
__author__ = 'florije'


class C:
    def __str__(self):
        return 'Class String'

    def do(self):
        return 'Class method'


def strf(*args):
    return 'Instance String', args


def doo(*args):
    return 'Instance Method'


if __name__ == '__main__':
    c = C()
    print(c)
    print(c.do())
    c.do = doo
    c.__str__ = strf
    print(c)
    print(c.do())
