#coding:utf-8

def complement(dna_string):
	dna_complement = {'a': 't',
	'g': 'c',
	't': 'a',
	'c': 'g'}
	comp_string = ''
	for base in dna_string:
		comp_string += dna_complement.get(base, 'a')
	return comp_string

dna_string = raw_input('Enter a DNA string file name:')
han = open(dna_string, 'r').read()
comp_string = complement(han)
print "Complement is:",comp_string