#conding:utf-8
def chese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanker. \n"

#我们可以直接给函数传递数字
print "We can just give the function numbers directly:"
chese_and_crackers(20,30)

#我们也可以使用变量
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
chese_and_crackers(amount_of_cheese,amount_of_crackers)

#我们也可以传递数学表达式
print "We can even do math inside too:"
chese_and_crackers(10 + 20, 5 + 6)

#我可以把变量和数学表达式合起来用
print "And we can combine the two, variables and math:"
chese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)