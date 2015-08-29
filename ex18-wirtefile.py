#coding:utf-8
"""
一个几百M的文本文件，需要每隔3行写到新的文件中
"""
with open('dist_1.txt','r')  as f1, open('dist_new.txt','w') as f2:
	i=0
	for line in f1:
		i += 1
		if i % 3 ==0:
			f2.write(line)