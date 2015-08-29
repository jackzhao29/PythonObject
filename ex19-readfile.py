#coding:utf-8
"""
从一个日志文本文件中，提取出其中的5到10行的数据
"""
i=0
file1=open("dist_1.txt","r")
file2=open("out.txt","w")
while True:
	line = file1.readline()
	i += 1
	if 5 <= i  and i <=10 :
		file2.write(line)
	if i > 10:
		break
	if not line:
		break
file1.close()
file2.close()