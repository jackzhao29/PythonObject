#coding:utf-8
from math import sqrt
'''
Python算法题
'''
'''
1.题目：有1、2、3、4个数组，能租车多个互不相同的且无重复数字的三位数？都是多少?
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。租车所有的排列后再去掉不满足条件的排列
'''
if __name__ == "__main__":
    sum = 0
    s = (1,2,3,4)
    for a in s:
        for b in s:
            for c in s:
                if a !=b and b!=c and c!=a:
                    print "%d%d%d" %(a,b,c)
                    sum+=1

    print "sum=",sum


'''
2.题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少?
程序分析：在10万以内判断，先将该数加上100后再开方，再加上268在开方，如果开方后的结果满足下列条件，即是结果
'''

if __name__ == "__main__":
    i = 1
    while i < 100000:
        a = int(sqrt(i + 100))
        b = int(sqrt(i + 268))
        if a ** 2 == (i+100) and b ** 2 == (i+268):
            print i
        i +=1


