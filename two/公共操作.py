#_*_ coding:utf-8 _*_
#@Time      :2020-11-2620:19
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :公共操作.py
#@Software:PyCharm

#  + 和并
# * 复制
# 元素是否存在 in
# 元素是否不存在 not in

# 字符串
str1 ="aa"
str2 ="bb"
str3 =str1 + str2
print(str3)

# 列表
list1 =[10,20]
list2 =[10,30]
lsit3 =list1 + list2
print(lsit3)

# 元组
s1 =(10,20)
s2=(1,2)
s3 =s1 + s2
print(s3)


# *
# 字符串
print("_"*10)

# 列表
list1= ["hello"]
print(list1 * 4)

# 元组

t1 =("world")

print(t1*4)

# in not in

# 字符串
print("a" in "abcd")
print("a" not in "abcd")

# 列表
list1 =['a','b','c','d']
print('a' in list1)
print("a" not in list1)

# 元组
t1 = ('a','b','c','d')
print('aa' in t1)
print('aa' not in t1)



# 公共方法

# len()计算容器中元素的个数
# de l或者del()删除
# max()返回容器中的最大值
# min（）返回容器中元素最小值
# range(start,end,step)
# enumerate()

# len()
# 1.字符串
str1 ="abcdef"
print(len(str1))

# 2.列表
list =[10,20,30]
print(len(list))

#  元组
t1 =(10,20,30,40,50)
print(len(t1))

# 集合
s1 ={10,20,30}
print(len(s1))


# 字典
dict1 = {'name':'tom','age':20}
print(len(dict1))


del()

# 1.字符串
str1 ='abcdef'
# del str1
# print(str1)

# 列表
list1 =[10,20,30,40]
del(list1[0])
print(list1)


# max()
# 字符串
str = 'adffjsdf'
print(max(str1))

# 列表
list1 =[10,20,30,40]
print(max(list1))

# min()
# 字符串
str1 ='abcdef'
print(min(str1))


# 列表
list1 =[10,20,30,40]
print(min(list1))



for i in range(1,10,1):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10):
    print(i)

    # range()生成的序列不包含end数字

# enumerate()
# ennmerate(可遍历对象，start=0)  start 是遍历下标，默认值是0
list = ['a','b','c','d','e']


for i in enumerate(list1):
    print(i)
for index,char in enumerate(list1,start=1):
    print(f"下标是{index},对应的字符是{char}")

tuple()
list1 =[10,20,30,40,50,20]
s1={100,200,300,400,500}
print(tuple(list1))
print(tuple(s1))

# list()


# list()

# t1 = ('a','b','c','d')
s1 = {100,200,300,400,500}
# print(list(t1))
print(list(s1))

# set ()
list =[10,20,30,40]
t1=(10,20,30,40)
print(set(list))
print(set(t1))
# 集合可以快速完成列表去重
# 2.集合不支持下标