#coding:utf-8
"""
python将list连续元素和非连续元素分开转换为指定字符串
list=[1,2,3,4,5,6,7,8,15,20,21,22,23,24,28,29,30,31,38]
写一个函数，让它返回如下的字符串
str='1-8,15,20-24,28-31,38'
"""

def continuous_str(lst):
    j = 0
    str1 = ''
    for i, item in enumerate(lst):
        if i > 0:
            if lst[i] != lst[i-1] + 1:
                tmp = lst[j:i]
                if len(tmp) == 1:
                    str1 += str(tmp[0]) + ','
                else:
                    str1 += str(tmp[0]) + "~" + str(tmp[-1]) + ','
                j = i
    tmp2 = lst[j:]
    if len(tmp2) == 1:
        str1 += str(tmp2[0]) + ','
    else:
        str1 += str(tmp2[0]) + "~" + str(tmp2[-1]) + ','

    return str1[:-1]

list = [1,2,3,4,5,6,7,8,15,20,21,22,23,24,28,29,30,31,38]
print continuous_str(list)