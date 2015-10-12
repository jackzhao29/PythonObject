#coding:utf-8
import time
"""
装饰器模式,‘@’语法糖精简装饰器代码
"""

def deco(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		mesecs = (endTime - startTime) * 1000
		print "-> elapsed time: %f ms" %mesecs
	return wrapper
@deco
def myfunc():
	print "start myfunc"
	time.sleep(0.6)
	print "end myfunc"

print "myfunc is:", myfunc.__name__
#如果使用@deco，就不需要重新给myfunc赋值了
#myfunc = deco(myfunc)
print "myfunc is:", myfunc.__name__
print myfunc()
