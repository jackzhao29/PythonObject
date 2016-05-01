#coding:utf-8
import random
from urllib import urlopen
import sys

WORD_URL="http://learncodethehardway.ort/words.txt"
WORDS=[]

PHRASES={
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\t def _init_(self,***)":
	"class %%% has-a _init_ that takes self and *** parameters.",
	"class %%%(object):\n\t def ***(self,@@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** functin, and call it with parameteres self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}

#keep going until the hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for sinppet in snippets:
			phrase = PHRASES[sinppet]
			print phrase

except EOFError:
	print "\nBye"