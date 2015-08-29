#coding:utf-8
"""
动态读取文件示例
"""
from sys import argv

script, fileName=argv

#打开fileName的文件
txt=open(fileName)

#打印文件名称
print "Here's your file %r:" % fileName
#读取文件内容并且打印
print txt.read()
#关闭文件
txt.close()

#打印提示信息
print "Type the fileName again:"
#打印提示符并且输入文件名称
file_again=raw_input(">")
#打开文件
txt_again=open(file_again)
#读取文件内容并且打印
print txt_again.read()
#关闭文件
txt_again.close()