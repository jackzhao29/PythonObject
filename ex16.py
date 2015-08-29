#coding:utf-8
"""
python函数是第一类对象，函数名可以赋值，可以作为函数参数传递
"""

def add(x, y):
	return x + y

def add_three_num(x, y, z, func):
	return func(func(x, y), z)

if __name__ == '__main__':
	print add_three_num(1,2,3,add)