#coding:utf-8
class B(object):
	def _init_(self):
		print 'B_init is called'
	def fun1(self):
		print 'B_fun1 is called'
		self.fun2()
		self.fun3()
	def fun2(self):
		print 'B_fun2 is called'
	def fun3(self):
		print 'B_fun3 is called'

class A(B):
	def _init_(self):
		super(A,self)._init_()
		print 'A_init is called'
	def fun2(self):
		super(A,self).fun2()
		print 'A_fun2 is called'
	def fun3(self):
		print 'A_fun3 is called'

if __name__ == '__main__':
	a= A()
	a.fun1()