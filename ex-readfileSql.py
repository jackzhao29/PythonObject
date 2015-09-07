#coding:utf-8
"""
读取文件input.txt内容,并且根据条件生成相应的SQL语句
将生成的SQL语句写入out.txt文件
input.txt文件内容如下：
,,value1,2015-09-07
test2,2015-09-07,value2,2015-09-07
test3,2015-09-07,value3,2015-09-07
test4,2015-09-07,,
,,test5,2015-09-07
"""
with open('input.txt','r') as f1, open('out.txt','w') as f2:
	for line in f1:
		strs=line.split(',')
		if len(strs[2]) > 0 and len(strs[1]) > 0:
			lines="update table set newValue='%s' where condition='%s';"  % (strs[2].strip(),strs[1].strip())
			f2.write(lines)
			f2.write("\n")
		           

f1.close()
f2.close()

print ("处理完毕")
