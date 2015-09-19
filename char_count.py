#coding:utf-8

"""
统计字符串中每个字符出现的次数
"""
mystring = 'helloword'
char_count = dict()
for char in mystring:
	count = char_count.get(char,0)
	count += 1
	char_count[char] = count

print char_count