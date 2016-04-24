#coding:utf-8

class MyStuff(object):
	"""docstring for MyStuff"""
	def __init__(self, arg):
		super(MyStuff, self).__init__()
		self.arg = arg

	def sing_me_song(self):
		for line in self.arg:
			print line
			


#use class example
happy_boday =  MyStuff(["Happy birthady to you",
	                   "I don't want to get sued",
	                   "So I'll stop right there"])


happy_boday.sing_me_song()
