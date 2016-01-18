# -*- coding: utf-8 -*-
__author__ = 'florije'

"""
>>> i = "asdf"
>>> j = "asdf"
>>> id(i) == id(j)
True
>>> i = 10000000000000000000000000000000
>>> j = 10000000000000000000000000000000
>>> id(j) == id(i)
False
>>> i = 4
>>> j = 4
>>> id(i) == id(j)
True
>>> class Kls:
...     pass
...
>>> k = Kls()
>>> j = Kls()
>>> id(k) == id(j)
False
"""