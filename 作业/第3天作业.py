#_*_ coding:utf-8 _*_
#@Time      :2020-12-1422:18
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :第3天作业.py
#@Software:PyCharm


# .把上次课的作业重新编程（不能看着答案，把分析过程写出来再敲代码）
# 	99乘法表；质数判断；三角形打印；斐波那契数列
"""
1.99乘法表
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6  3*3=9
1*4=4 2*4=8  3*4=12 4*4=16
1*5=5 2*5=10 3*5=15 4*5=20  5*5=25
1*6=6 2*6=12 3*6=18 4*6=24  5*6=30  6*6=36
1*7=7 2*7=14 3*7=21 4*7=28  5*6=30  6*7=42 7*7=49
1*8=8 2*8=16 3*8=24 4*8=32  5*6=30  6*8=48 7*8=56  8*8=64
1*9=8 2*9=18 3*9=27 4*9=36  5*6=30  6*9=54 7*9=63  8*9=72  9*9=81

9行  表示行
表达式a*b =a*b

"""
# j =0
# while j <=9:
#     i =1
#     while i<=j:
#         print(f"{i}*{j}={j*i}",end='')
#         i +=1
#     print()
#
#     j +=1
'''''
质数：只能被1和他本身整除,不能整除则不是质数
    



'''
# num =int(input("输入一个数"))
# n=2
# while n<num:
#     if num % n ==0:
#         print("不是质数")
#         break
#
#     n +=1
#
# else:
#     print("num是质数")


# 打印正角形
'''''
*****
*****
*****
*****

'''
# 第一种
# j=0
# while j<=5:
#
#     i =0
#     while i<=5:
#         print("*",end="")
#
#         i  +=1
#
#     print()
#
#     j +=1

# 第二种
# for i in range(0,5):
#     print("*" * 5)




#  打印三角形

''''

*
**
***
****
4行
*号是内循环

'''
# 第一种
# j=0
# while j<5:
#     i =0
#
#     while i<j:
#         print("*",end="")
#
#         i +=1
#
#     print()
#     j +=1
# 第二种
# for i in range(0,5):
#     print(i*"*")

''''
****
***
**
*
星号内循环
每行减少一个

'''
# j=5
# while j>0:
#     i=0
#     while i<j:
#         print("*",end='')
#         i +=1
#
#     print()
#     j -=1

# 第二种
# for i in range(0,5):
#     print((5-i)*"*")

''''
右对齐三角形


   *
  **
 *** 
**** 

a 表示行 b 表示空格 c表示星号
a=1  b=3  c =1
a=2  b=2  c=2
a=3  b=1  c=3
a=4  b=0  c =4
a+b=4
b =4-a

'''

# 第一种
a=0

while  a<5:

    b =0
    while b<5-a:
        print(" ",end="")

        b+=1

    c =0
    while c <a:
        print("*",end="")
        c +=1
    print()
    a+=1

#第2种

for i in range(0,5):
    print((5-i)*" "+i*"*")



''''
右对齐倒三角形


*****
 ****  
  *** 
   ** 
    * 
a 表示行 b 表示星号  c表示空格
a=1  b=5 c =0
a=2  b=4  c=1
a=3  b=3  c=2
a=4  b=2 c =3
a=5  b=1  c =4
a+b =6  a-c=1
b =6-a  c=a-1

'''


# a= 0
# while a<=5:
#     b =0
#     while b<=a-1:
#         print(" ",end="")
#         b+=1
#     c =0
#     while c<6-a:
#         print("*",end="")
#         c+=1
#
#     print()
#     a += 1
# # 右对齐倒三角形
# for i in range(5):
#     print(i*" " + (5-i)*'*')




# 2.打印由*组成的菱形，该菱形一共7行，已在群里发了，大家自己找图


# 3.使用列表推导式生成能被5整除的数（100以内）
# list1=[]
# for i in range(0,101):
#     if i%5==0:
#         list1.append(i)
#
#     print(list1)

# list1 =[i for i in range(0,101) if i%5==0]
# print(list1)

# 4.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
# name =['xioaming','xiaohong','zahngsan']
# age =[19,20,30]
#
# dict1={}
#
# print(name[0])
#
# for i in range(len(name)):
#     dict1[name[i]]=age[i]
#     print(dict1)
#
# 5.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},xxx]
# ----------------
# *   1-新增用户
# *   2-查询用户
# *   3-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息
# print("[{name:xxx,age:xxx},xxx]")
def yemian():
    print(" ----------------")
    print(' *   1-新增用户')
    print(' *   2-查询用户')
    print(' *   3-删除用户')
    print(" ----------------")

list=[]
def login_w():
    global  list
    a =input("输入姓名：")
    b = input("输入年龄：")
    dict1={}
    dict1['name']=a
    dict1['age']=b
    list.append(dict1)
    for  i in list:
        if i['name']==a:
            print("用户已存在")
            break
def cha():
    global list
    c =input("请输入要查询的用户：")
    for i in list:
        if i['name']==c:
            print(i)
def sel():
    global list

    d= input("请输入要删除的用户：")
    for i in list:
        if i['name']==d:
            print("删除成功")



login_w()
cha()
sel()
yemian()