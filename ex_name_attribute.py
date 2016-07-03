#coding:utf-8
"""
有的对象有__name__属性，直接可以取得
"""
class Foo(object):
    pass

    def foo():
        pass


print Foo.__name__
