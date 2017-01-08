#coding:utf-8
"""
没有__name__属性的对象，用globals()取得
"""

class Foo(object):
    pass

    variable = [1, 2, 3, 4]
    d = globals()

    for key in d.copy():
        if type(d[key]) is type(variable) and d[key] == variable:
            print(key, type(key))
