#coding:utf-8
from sys import argv
'''
多态（英语：Polymorphism），是指面向对象程序运行时，相同的消息可能会送给多个不同的类之对象，
而系统可依据对象所属类，引发对应类的方法，而有不同的行为。
简单来说，所谓多态意指相同的消息给予不同的对象会引发不同的动作称之。
在面向对象程序设计中，多态一般指子类型多态（Subtype polymorphism）。
 
上面的定义有点让初学者费解，用“打开”这个动作来描述面向对象的多态。
"打开"，可以是打开门，打开窗户，打开书等等。"打开"这个动作，碰到不同的对象门，窗户，书，有不同的行为模式。
这个就是多态。
'''
# 例1
script,param=argv
class Door(object):
	def  open(self):
		print "打开门"

class Window(object):
	def open(self):
		print "打开窗"

class Book(object):
	def open(self):
		print "打开书"

lst=[Door(),Window(),Book()]
print (param)
for item in lst:
	if param == 'window':
		item.open()
	else:
		print "参数不对"





