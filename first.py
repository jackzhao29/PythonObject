#coding:utf-8

"""
模块可导入和可执行的
建议模块都用上 if __name__ == '__main__':
	main()
"""
def main():
	print "欢迎执行main方法"

if __name__ == '__main__':
	print "从命令行开始执行"
	main()

"""
判断结构或循环结果等中，直接判断变量是不是True或False
"""

name = 'Safe'
pets = ['Dog','Cat','Hamster']
owners = {'Safe':'Cat','George':'Dog'}
if name and pets and owners:
	print ('We have pets!')

"""
尽可能用in
"""
company_name = '人生苦短，学会python'
if company_name.find('短') != -1:
	print "公司名中有{0}".format("端")

"""
for x in items:
"""
pets = ['Dog', 'Cat','Hamstr']
for pet in pets:
	print ('A',pet, 'can be very cute!')

"""
交换值不需要中间变量
a,b=b,a
"""
a, b =5, 6
print (a, b)
a, b= b, a
print (a, b)

"""
从序列中构建字符串
''.json(some_strings)
"""
chars = ['s', 'a', 'f', 'e']
name = ''.join(chars)
print (name) 

"""
异常判断
"""
d = {'x':'s'}
try:
	value =int(d['x'])
	print ('try',value)
except(KeyError,TypeError,ValueError):
	value = None
	print value

"""
用内置方法enumerate
for i,item in enumerate(items):
"""
names = ['Safe', 'George', 'Mildred']
for i,name in enumerate(names):
	print(i,name)

"""
用列表解析
"""
data = [7, 20, 3, 15, 11]
result = [i * 3 for i in data if i>10]
print (result)

"""
从有key和values的list，用zip创建字典
"""
keys = ['1','2','3']
values = ['python','golang','php']
d=dict(zip(keys,values))
print (d)
