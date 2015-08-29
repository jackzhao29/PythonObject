#coding:utf-8
"""
Fibonacci数列定义：
F0=0                      (n=0)
F1=1                      (n=1)
Fn=F(n-1)+F(n-2)  (n>=2)
"""

#递归，根据定义直接写
#这种方法不是一个好方法，因为它的开销太大，比较计算fib(1000)，就需要耐心等待较长一段时间了
def fib(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#递归，进行初始化
#fib慢，就是因为每次都要计算前面已经算过的项，这里将上述算法进行稍微改进

memo = {0:0, 1:1}
def fib2(n):
	if not n in memo:
		memo[n] = fib2(n-1) + fib2(n-2)
	return memo[n]

#迭代
def fib3(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a

if __name__ == '__main__':
	print(fib(8))
	print(fib2(8))
	print(fib3(8))