#coding:utf-8

def match_dna(query, sequence):
	if query in sequence:
		return True
	else:
		return False

mydna = 'gaaacctta'
myquery = 'ac'
if match_dna(myquery, mydna):
	print "Yay it matches"
else:
	print "No it does't match"