# coding:utf-8
'''
闭包
'''
def make_even_generator():
	i=[0];

	def inner():
		i[0] +=2
		return i[0]
	return inner

foo=make_even_generator()
print foo()
print foo()
print foo()
print foo()
		