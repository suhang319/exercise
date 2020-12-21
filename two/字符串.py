#_*_ coding:utf-8 _*_
#@Time      :2020-11-2319:06
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :字符串.py
#@Software:PyCharm
1.# 创建字符串
a ='dfsdkkd'


name='Tom'
print("我的名字是%s" % name)
print(f"我的名字是{name}")

# name =input("请输入您的名字：")
# print(f"您输入的名字是{name}")
# print(type(name))

# 下标  从0开始
name='afgdskfdksfk'
print(name[0])
print(name[1])

name='abcdefghy'
# 序列[开始位置下标：结束位置下标：步长]
# 不包含结束位置下标对应的数据，正负数均可
# 步长是选取间隔，正负整数均可，默认步长为1
print(name[2:5:1])
print(name[2:5])
print(name[:5])
print(name[:])
print(name[2:])
print(name[:-1])
print(name[-4:-1])


# 查找
# find（）查找字串在字符串中是否存在，返回下标即存在，返回-1即存不存在。
# 语法 字符串序列.find(子串，开始下标，结束位置下标)

mystr =' hello world and superctest and chaoge and python '

print(mystr.find('and'))
print(mystr.find('and',15,36))
print(mystr.find("andf"))

# index()查找，如果子串在字符串中，则返回下标，如果不在则报错
# 语法 字符串序列.index(子串，开始位置下标，结束位置下标)
mystr =' hello world and superctest and chaoge and python '
print(mystr.index('and'))
print(mystr.index("and",10,35))
# print(mystr.index("sdf"))
# rfind()和find()功能相同，查找方向从右侧开始
# rindex()和index()功能相同，查找从右侧开始

# count()返回子串在字符串中出现的次数
# 用法 字符串序列.count(子串，开始下标位置，结束下标位置）
mystr =' hello world and superctest and chaoge and python '
print(mystr.count("and"))
print(mystr.count('and',10,39))


# 修改 replace()
# 用法 字符串序列.replace(旧子串，新子串，替换次数)
# 数据按照是否直接修改分为可变类型和不可变类型，字符串修改的时候不能改变原有的字符串，属于不能直接修改的类型，不可变类型
mystr =' hello world and superctest and chaoge and python '
print(mystr.replace('and',"he"))
print(mystr.replace("and",'he',2))
print(mystr.replace('and','he',10))

# split()按指定字符分割字符串
# 用法 字符串序列.split(分割字符，num)
# num为分割字符出现的次数，返回则为num+1个
# 分割是分割原有字符串中的子串，分割后丢失该字符串
mystr =' hello world and superctest and chaoge and python '
print(mystr.split('and'))
print(mystr.split("and",2))
print(mystr.split(' '))
print(mystr.split(" ",2))
# join() 用于一个字符和子串合并字符串，将多个字符串合并为新的字符串

# 用法 字符或者子串.join(多字符串组成的序列)

list1 =['chao','ge','test','promotion']
t1 = ('aa','b','cc','ddd')

print("_".join(list1))
print('...'.join(t1))

# capitalize()将字符串第一个转换为大写
mystr =' hello world and superctest and chaoge and python '
print(mystr.capitalize())

# title()将字符串中每个字符串的首字母都大写

print(mystr.title())
mystr =' Hello world and superctest and chaoge and python '
# lower()将字符串中大写转为小写
print(mystr.lower())

# ljust() 返回一个原字符串左对齐，并使用指定的新字符填充
# 语法 字符串序列.liust(长度，填充字符）
mystr ='hello'
print(mystr.ljust(10,','))

# rjust()返回一个原字符串右对齐，新的字符填充
mystr2='helkkf'
print(mystr2.rjust(10,'_'))

# center()返回一个居中对齐
mystr3= 'hekkkfj'
print(mystr3.center(10,' '))
print(mystr.center(10,'.'))

# 判断 startswith 检查字符串是否已子串开头，是的话返回True,不是返回Flase,加上开始和结束位置下标，在该区间内查找
# 用法 字符串序列.startswith('子字符串'，开始位置下标，结束位置下标)
mystr ='hello world and superctest and chaoge and python '
print(mystr.startswith('hello'))
print(mystr.startswith('hello',5,10))

# endswith()检查一个字符串是否已该子串结尾，是的话返回True,不是返回Flase,加上开始和结束位置下标，在该区间内查找
# 用法 字符串序列.endswith()
mystr ='hello world and superctest and chaoge and python'
print(mystr.endswith('python'))
print(mystr.endswith('python',5,20))

# isalpha()字符串中有一个字符且所有字符都为字母，返回True 否则返回False
mystr ="hello"
mystr1="hello334"
print(mystr.isalpha())
print(mystr1.isalpha())

# isdigit()字符串中字符为数字，返回True 否则返回False
mystr3= '4234344'
mystr6='23443fjfjfj'
print(mystr3.isdigit())
print(mystr6.isdigit())

# isalnum()字符串中有字母和数字，返回真，否则为假
mystr6 = '3223ef'
mystr='dkskdd_'
print(mystr6.isalnum())
print(mystr.isalnum())

# isspace():只包含空白，返回真
mystr3= '1 2 3 4 5'
mystr2 = '   '
print(mystr3.isspace())
print(mystr2.isspace())
