#coding:utf-8
"""
函数创建，调用，使用
"""
#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2, arg3=args
	print "arg1: %r, arg2: %r, arg3: %r" % (arg1,arg2, arg3)

#ok, that  *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I go nothin"

print_two("Ted", "Shaw", "Thress")
print_two_again("Ted", "Shaw")
print_one("jack")
print_none()