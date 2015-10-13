#coding:utf-8
__author__ = 'coldface'

#modulo
remainder = 11 % 3
print(remainder)

#power
square = 4 ** 2 #=16
print 'square=',square
cubed = 2 ** 3 #=8
print 'cubed=',cubed

#operator is overridden for Strings
dopleHertz = "Hertz" * 2
print(dopleHertz)

#operator is overridden for Lists
list1 = [1, 11, 111]
list2 = [2, 22, 222]

joinList = list1+list2
print ("Join List")
for i in joinList:
	print i

#+operator is overridden for Lists
multiList = list1 * 5
print "List * 5"
for i in multiList:
	print i
