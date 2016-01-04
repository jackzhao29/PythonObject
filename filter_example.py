# coding:utf-8
lst = [1,2,3,4,5,6,7,8,9]
#所有奇数都返回true，偶数返回false被过滤掉
print filter(lambda x: x % 2 !=0, lst)
