#coding:utf-8
'''
正则表达式练习
1.正则表达式的语法
1.1.单个字符
.        任意的一个字符
a|b      字符a或者字符b
[afg]    a或者f或者g的一个字符
[0-4]    0-4范围内的一个字符
[a-f]    a-f范围内的一个字符
[^m]     不是m的一个字符
\s       一个空格
\S       一个非空格
\d       [0-9]
\D       [^0-9]
\w       [0-9a-zA-Z]
\W       [^0-9a-zA-Z]

1.2.重复(紧跟在单个字符之后，表示多个这样类似的字符)
*       重复 >=0 次
+       重复 >=1 次
?       重复 0或者1 次
{m}     重复m此，比如说a{4}相当于aaaa,再比如谁[1-3]{2}相当于[1-3][1-3]
{m, n}  重复m到n次，比如说a{2, 5}表示a重复2到5次，小于m次的重复，或者大于n此的重复都不符合条件

正则表达        相符的字符串举例
[0-9]{3, 5}     9678
a?b             b
a+b             aaaaab

1.3.位置
^     字符串的起始位置
$     字符串的结束位置

正则表达        相符的字符串举例
^ab.*c$         abeec
re.search(pattern, string) #搜索整个字符串，直到发现符合的子字符串
re.match(pattern, string) #从头开始检查字符串是否符合正则表达式，必须从字符串的第一个字符开始就相符
re.sub(pattern ,replacement, string) #在string中利用正则变换pattern进线搜索，对于搜索到的字符串，用另一字符串replacement替换，返回替换后的字符串
re.split() #根据正则表达式分隔字符串，将分隔后的所有子字符串放在一个表(list)中返回
re.findall() #根据正则表达式搜索字符串，将所有符合的子字符串放在一个表(list)中返回
'''
import re,os,datetime
m = re.search('[0-9]','abcd4ef23b')
print (m.group(0))
p = re.findall('[0-9]','abcd4ef23b')
print (p)

'''
群(group)概念

output_(\d{4})

该正则表达式用括号()包围了一个小的正则表达式，\d{4}。 这个小的正则表达式被用于从结果中筛选想要的信息（在这里是四位数字）。这样被括号圈起来的正则表达式的一部分，称为群(group)。
我们可以m.group(number)的方法来查询群。group(0)是整个正则表达的搜索结果，group(1)是第一个群…
'''

m = re.search("output_(\d{4})","output_1986.txt")
print (m.group(1))

#可以将群命名
m = re.search("output_(?P<year>\d{4})","output_1986.txt")
print (m.group("year"))

m = re.search("(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})\.","output_1981.10.21.txt")
print (m.group("year"),m.group("month"),m.group("day"))
year = m.group("year")
month = m.group("month")
day = m.group("day")
date = datetime.date(int(year),int(month),int(day))
print (date)
wd = date.weekday()+1
print (wd)
os.rename("output_1981.10.21.txt","output_"+year+"-"+month+"-"+day+"-"+str(wd)+".txt")
