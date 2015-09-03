#coding:utf-8
import time
start_time=time.time()

def find_ip(path):
	for line in open(path):
		s=line.find('web')
		print s
		if s >= 0:
			yield line[:s].strip()

p=find_ip("bigfile.txt")
p=list(set(list(p)))

for item in p:
	print item

print time.time()-start_time, "seconds"