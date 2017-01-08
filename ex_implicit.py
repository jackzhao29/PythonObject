#coding:utf-8
#继承的例子
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
dad.implicit()
