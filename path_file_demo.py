#coding=utf-8
'''路径与文件'''

import os.path
import sys
import glob
type = sys.getfilesystemencoding()
path ='/Users/coldface/Documents/test.txt'

#查询路径中包含的文件名
print(os.path.basename(path))
#查询路径中包含的目录
print(os.path.dirname(path))
#将路径分割成文件名和目录两部分，放在一个表中返回
info = os.path.split(path)
#使用目录名和文件名构成一个路径字符串
path2 = os.path.join('/','Users','coldface','Documents','dist_1.txt')

p_list = [path,path2]
#查询多个路径的共同部分
print(os.path.commonprefix(p_list))

#去除路径path中的冗余
#path = "/home/coldface/../."
print(os.path.normpath(path))

#查询相关文件信息
#查询文件是否存在
s = "查询文件是否存在"
print(s.decode('utf-8').encode(type),os.path.exists(path))
#查询文件大小
print("查询文件大小=",os.path.getsize(path))
#查询文件上一次读取时间
print("查询文件上一次读取时间=",os.path.getatime(path))
#查询文件上一次修改时间
print("查询文件上一次修改时间=",os.path.getmtime(path))
#路径是否指向常规文件
print("路径是否指向常规文件=",os.path.isfile(path))
#路径是否指向目录文件
print("路径是否指向目录文件=",os.path.isdir(path))

#查找目录下的所有文件
print(glob.glob("/Users/coldface/Documents/*"))
