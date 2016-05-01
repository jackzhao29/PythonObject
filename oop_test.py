#coding:utf-8
import random
from urllib import urlopen
import sys

WORD_URL="http://learncodethehardway.org/words.txt"
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

#do they want to drill phrasses first
PhRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[i] == "english":
	PhRASE_FIRST=True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet,phrase):
	class_names = [w.capitalize() for w in 
	              random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in rang(0, snippet.count("@@@")):
    	param_count = random.randint(1, 3)
    	param_names.append(', '.join(random.sample(WORD_URL, param_count)))

    for sentence in snippet, phrase:
    	result = sentence[:]

    #fake class names
    for word in class_names:
    	result = result.replace("@@@", word, 1)

    #fake other names
    for word in param_names:
    	result = result.replace("@@@", word, 1)

    results.append(result)
    return results


#keep going until the hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for sinppet in snippets:
			phrase = PHRASES[sinppet]
			question, answer = convert(snippet, phrase)
			if PhRASE_FIRST:
				question, answer = answer, question
			print question

			raw_input(">")
			print "ANSWER: %s\n\n" % answer

except EOFError:
	print "\nBye"