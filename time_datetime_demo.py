#coding:utf-8
'''
time包
datetime包
'''
import time
import datetime 
print (time.time())
print (time.clock())

print("start...")
#time.sleep(10)
print("wake up")

st = time.gmtime()
print ("st",st)
st = time.localtime()
print (st)
s = time.mktime(st)
print (s)

t = datetime.datetime(2017,01,15,20,31,00)
print (t)

#timedelat:时间间隔对象

t = datetime.datetime(2017,01,15,20,33,00)
t_next = datetime.datetime(2017,01,15,9,00,00)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print (t + delta1)
print (t + delta2)
print (t_next - t)

#两个datetime对象可以进行比较
a = t > t_next
print (a)

from datetime import datetime

#将时间字符串转换成datetime对象
format ="output-%Y-%m-%d-%H%M%S.txt"
str = "output-2017-01-15-030000.txt"
t = datetime.strptime(str,format)
print (t)
#将datetime对象转换成时间字符串
print (t_next.strftime(format))
