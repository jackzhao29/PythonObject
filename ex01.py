# coding:utf-8
"""
函数返回一个匿名函数，赋值给p，p是一个函数，函数带括号调用。
"""
def _not_divisible(n):
     return lambda x: x%n>0

p= _not_divisible(10)
print p(5)