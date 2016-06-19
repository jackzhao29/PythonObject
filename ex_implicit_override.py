#coding:utf-8
'''
有时候需要让子类里的函数有一个不同的行为，这种情况下隐式继承是做不到的，二需要覆盖子类中的函数，从而实现它的新功能。只要在子类Child中定义一个相同的名称的函数就可以了。
'''
class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override"

dad = Parent()
son = Child()

dad.override()
son.override()
