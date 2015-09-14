#coding:utf-8
"""
使用==以及一个新的python词汇return来将变量设置为一个函数的值
"""
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACT %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDE %d / %d" % (a, b)
	return a / b

print "Let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

print "Here is apuzzle."

what = add(age,subtract(height,multiply(weight,divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"