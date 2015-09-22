#coding:utf-8

myfile = open('out.txt')
line_pos = []

mypos = myfile.tell()
line_pos.append(mypos)
print 'myfile.tell:', mypos

line = myfile.readline()
print 'myfile.readline:', line

while line != '':
	mypos=myfile.tell()
	line_pos.append(mypos)
	line = myfile.readline()

print line_pos

filecontent = open('out.txt')
line_content = filecontent.readline()
list = []
while  line_content != '':
	print line_content
	list.append(line_content)
	line_content = filecontent.readline()

print list

