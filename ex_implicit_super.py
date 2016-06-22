#coding:utf-8
'''
继承的第三种方法是一个覆盖的特例，使用python内置的函数来在运行前或运行后修改行为。
'''
class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD,BEFORE PARENT altered()"
        super(Child,self).altered()
        print "ChILD,ATGER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
