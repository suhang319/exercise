#_*_ coding:utf-8 _*_
#@Time      :2020-11-2921:17
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :g.py
#@Software:PyCharm

# name = input('请输入您的名字')
# print(f"你输入的名字是{name}")
# print(type(name))
#
# pawwword = input("请输入您的密码：")
# print(f"你输入的密码是：{pawwword}")
# print(type(pawwword))

# 下标
name ='fkfkkf'
print(name[0])
print(name[1])

# 切片 序列[开始位置下标，结束位置下标：步长]
# 不包含结束位置下标对应的数据，正负数均可
# 步长是选取间隔，正负数均可，默认为1


name ="assdfdgsg"
print(name[2:5])
print(name[2:5:1])
print(name[:5])
print(name[1:])
print(name[:])
print(name[::2])
print(name[:-1])
  # 负1表示倒数第一个数
print(name[-4:-1])

# 查找find()
# 字符串序列.find(子串，开始位置下标，结束位置下标)
# 开始和结束位置下标可以省略，表示在整个字符串序列中查找,不存在返回-1，存在返回下标


mystr= "hello world and superctrst and chaoge and python"
print(mystr.find('and'))
print(mystr.find("and",15,30))
print(mystr.find("ands"))

# vip8 ='su su xiaoming lisi'
# name= input("请输入您的名字：")
# result=vip8.find(name)
# if result==-1:
#     print("不在班级")
# else:
#     print("在我们班")


# index()
# 检测某个子串是否包含在这个字符串中，如果返回这个子串
# 用法 字符串序列.index(子串，开始位置下标，结束位置下标)
mystr="hello world and superctrst and chaoge python "
print(mystr.index("and"))
print(mystr.index("and",10,20))
# print(mystr.index("andd"))

print(mystr.rfind('and'))
print(mystr.rindex("and"))
# count()开始和结束位置下标可以省略，表示整个字符串序列中查找
# 用法  字符串序列.(子串，开始位置下标，结束位置下标)
mystr="hello world and superctrst and chaoge python "
print(mystr.count("and"))
print(mystr.count("as"))
print(mystr.count("and",0,20))

# 修改
# replace()
# 用法 字符串序列.replace(旧子串，新子串，替换次数)
mystr = 'hello worla and supertest and chaoge  and python '
print(mystr.replace("and",'he'))
print(mystr.replace("and",'he',10))
# 数据按照是否直接修改分为可变类型和不可变类型，字符串类型数据修改的时候不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型
# 。

# split()按照指定字符分割字符串
# 用法  字符串序列.split(分割字符，num)
mystr =" hello world and supertest and chaoge and python"
print(mystr.split("and"))
print(mystr.split("and",2))
print(mystr.split(" "))
print(mystr.split(" ",2))

# join()用于一个字符或者子串合并字符串，多个字符串合并成一个新的字符串

# 语法
# 字符或者子串.join(多字符串组成的序列)

list1 =['chaoge ','ge ', 'twe', 'promotion']
t1=('aa' ,'bb','cc','dd')

print("_".join(list1))
print('.'.join(t1))
print(" ".join(t1))
# capitalize
mystr ="hello world and supertest and chaoge and python"
print(mystr.capitalize())
# title()
mystr ="hello world and supertest and chaoge and python"
print(mystr.title())

# lower()大写转换小写
mystr ="Hello World And Supertest And Chaoge And Python"
print(mystr.lower())

# upper()小写转换大写
mystr ="hello world and supertest and chaoge and python"
print(mystr.upper())

# lstrip()
# 删除左侧空白字符
# rstrip()
# 删除右侧空白字符

# strip()
# 删除俩侧空白字符


# ljust()返回一个原字符串左对齐，并使用指定字符
# 用法 字符串序列.ljust(长度，填充字符)
mystr = "hello"
print(mystr.ljust(10,'.'))

# rjust()返回一个原字符串左对齐，并使用指定字符
# 用法 字符串序列.rjust(长度，填充字符)

# center()居中对齐
mystr = "hello"
print(mystr.center(10,'.'))

# 字符串序列.startswith(子串，开始位置下标，结束位置下标)
mystr ="hello world and supertest and chaoge and python"
print(mystr.startswith("hello"))
print(mystr.startswith('hello',5,20))
# 字符串序列.endswith(子串，开始位置下标，结束位置下标)

# isalpha()所有字符都是字母 返回真
# isdigit()数字到那会真
# isalnum()字母或者数字，为真
# isspace()字符串中包含空白，为真


# name= input("从键盘输入一个姓名")
# classname='suahng lisi lisi xioaming'
# if classname.find(name)!=-1:
#     if classname.count(name)>1:
#         print(f"有重名，重名人数{classname.count(name)}")
#     else:
#         print("无冲明")
# else:
#     print("不存在")


name_list =['TOM','LIYI','ROSE']
print(name_list[0])
print(name_list[1])

print(name_list.index('TOM'))
print(name_list.index('TOM',0,2))


print(name_list.count("TOM"))

# len() 长度 列表的中数据个数
print(len(name_list))

name_list =['TOM','LIYI','ROSE']
print("tom" in name_list )


name_list.append("xiamong")
print(name_list)

# extend（）列表结尾追加数据，如果数据是一个序列，则这个序列添加到列表里
# 语法 列表序列.extend(数据)
name_list =['TOM','LIYI','ROSE']
name_list.extend("xiaoming")
print(name_list)

# insert()指定位置新增数据
# 语法
# 列表序列.insert(位置下标，数据)
name_list =['TOM','LIYI','ROSE']
name_list.insert(1,"dfff")
print(name_list)

name_list=['tom','lilt','rose']
# del name_list
print(name_list)
del name_list[0]
print(name_list)

# 删除指定下标的数据(默认为最后一个)，并返回该数据
# 列表序列.pop(下标)
name_list=['tom','lilt','rose']
print(name_list.pop())
print(name_list)
# remove 移除列表中某个数据的第一个匹配项
# 列表序列.remove(数据)
name_list=['tom','lilt','rose']
name_list.remove("rose")
print(name_list)

# clear()清空列表

name_list=['tom','lilt','rose']
name_list.clear()
print(name_list)


# 修改
name_list=['tom','lilt','rose']
name_list[2]='fff'
print(name_list)


# 逆置
nme_list=[1,5,2,3,6,8]
nme_list.reverse()
print(nme_list)

# sort()排序
# 列表序列.sort()
num_list=[1,5,2,3,46,6]
print(num_list)

num_list=[1,5,2,3,46,6]
num_list2=num_list.copy()
print(num_list2)


# 元组

t1 =(10,20,30)
t2=(20,)
print(type(t2))

# 元组不支持修改
tuple =('aa','bb','cc')
print(tuple[0])

tuple =('aa','bb','cc')
print(tuple.index("aa"))

tuple =('aa','bb','cc','cc')
print(tuple.count("cc"))

tuple =('aa','bb','cc','cc')
print(len(tuple))


res2=['中国银行']
result=res2[0]
print(type(result))

dict1={'name':'TOM','AGE':20,'gender':'男'}

dict2={}

# 增 字典序列[key]=值

dict1={'name':'TOM','AGE':20,'gender':'男'}
dict1['name']='er'
print(dict1)

dict1['id']=10
print(dict1)

# 删除 del()
dict1={'name':'TOM','AGE':20,'gender':'男'}
del  dict1['gender']
print(dict1)


# clear()
dict1.clear()
print(dict1)
# 查找
dict1={'name':'TOM','AGE':20,'gender':'男'}
print(dict1['name'])
# print(dict1['id'])


dict1={'name':'TOM','AGE':20,'gender':'男'}
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))

dict1={'name':'TOM','AGE':20,'gender':'男'}
print(dict1.keys())

dict1={'name':'TOM','AGE':20,'gender':'男'}
print(dict1.values())

dict1={'name':'TOM','AGE':20,'gender':'男'}
print(dict1.items())

dict1={'name':'TOM','AGE':20,'gender':'男'}
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)


    # 遍历字典的元素
dict1 = {'name': 'TOM', 'AGE': 20, 'gender': '男'}
for item in dict1.items():
    print(item)

dict1 = {'name': 'TOM', 'AGE': 20, 'gender': '男'}
for key,value in dict1.items():
    print(f'{key}={value}')


# 集合

s2 ={23,34,45,56,67}

print(s2)
# 空集合
set()
s3 =set("fsdfsf")
# 集合是无序的，可以去重
print(s3)

s1 ={10,20}
s1.add('12')
print(s1)
s1 ={10,20,30,40,50}

s1.update([100,200])
s1.update('abc')
print(s1)

s1.remove(10)
print(s1)

s1 ={10,20}
s1.discard(10)
print(s1)

s1.discard(10)
print(s1)

s1 ={10,20,30,40,50}

del_num =s1.pop()
print(del_num)
print(s1)

s1 ={10,20,30,40,50}
print(10 in s1)
print(10 not in s1)



str1 ='aa'
str2='ff'
str3= str1 + str2
print(str3)

lis1=[10,20]
list2=[30,20]
list3= lis1+ list2
print(list3)

t1=(10,20)
t2=(20,30)
t3= t1 +t2
print(t3)

print("*" * 10)
list =['hello']
print(list * 4)

# in not in
print('a' in "abds")
print('a' not in 'absd')

t1 =('a','b','c')
print("a" in t1)
print('aa' not in t1)

list1 =[10,20,30]
print(10 in list1)

str1 ="fdsfsdfs"
print (len(str1))


# del
str1 ='sdfdsg'
del str1
# print(str1)


list1 =[10,20,30,40]
del(list1[0])
print(list1)


# max()
str1 ='afsdfs'
print(max(str1))


list1 =[10,20,30]
print(min(list1))

for i in range(1,10,1):
    print(i)


list1 = ['a','b','c','d']

for i in enumerate(list1):

    print(i)

for index,char in enumerate(list1,start=1):
    print(f'下标{index},对应的字符是{char}')


name =['TOM']
# name.remove('a')

name.pop(3)
