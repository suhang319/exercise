#_*_ coding:utf-8 _*_
#@Time      :2020-11-2914:24
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :从新复习.py
#@Software:PyCharm

# 单行注释
# print("hello word ")

'''

多行注释 三个单引号或者三个双引号
'''

a = 5
print(id(5))

MyName = "suhang"

print(MyName)


a =1
print(type(a))
b =1.1
print(type(b))
c =True
print(type(c))
d ="12345"
print(type(d))
e =[1,2,3,4]
print(type(e))
f =(1,2,3,4,5)
print(type(f))
h ={122,200,300}
print(type(h))
set()
j = {'name':"suahng",'age':20}
print(type(j))


a =5

print("我今年",a,'岁了')
print("我今年%d岁了" % a)

b =6
c =a/b
print("%f"% c)
print("%.1f" % c)

age =18
name ="tom"
weight =75.5
student_id=1
print("我的名字是%s" % name)
print('我的序号是%4d' % student_id)
print("我的体重是%.2f" % weight)
print("我的名字是%s,今年%d岁了" % (name,age))
print("我的名字是%s,明年%d岁了" % (name,age+1))
print(f"我的名字是{name},明年{age + 1}岁了")
# \n 换行
# \t 制表符

# a = int(input('请输入一个数:'))
#
# print("您输入的数字是：")
#
# num = input("请输入您的幸运数字：")
#
# print(f"您输入的幸运数字是{num}")

# print(type(num))
#
# print(type(int(num)))

# int转换成浮点型
num=1
print(type(num))
print(float(num))
print(type(float(num)))

num1 =10
print(str(num1))
print(type(str(num1)))

list1=[10,20,30]
print(type(list1))
print(tuple(list1))
print(type(tuple(list1)))

t1=(10,20,30)
print(type(t1))
print(list(t1))
print(type(list(t1)))

# eval()
str1="10"
str2='[1,2,3]'
str3="(100,200,300)"
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

age = int(input('请输入您的年龄：'))

if age >=18:
    print(f"您输入的年龄是{age},已成年，可以上网")
print("关闭")

"""
money = 1 表示有钱  money=0表示没钱
saet = 1表示有座，seat=0表示没座
判断是否有钱：
    1.1有钱可以上车
        2判断是否有座
            2.1有座可以坐下
            2.2没座位

    1.2没钱不能上车

"""
money =int(input("输入钱数"))
seat= int(input("输入座位数"))
if money==1:
    print("有钱可以上车")
    if seat ==1:
        print("有座位可以坐下")
    else:
        print("没座位")
else:
    print("没钱")


import random
b = random.randint(0,3)

'''



'''
a =int(input("请输入玩家1.石头2.剪刀3.布"))

if (a==1 and b==2) or (a==2 and b==3) or (a== 3 and b== 1):
    print("玩家胜利")
elif a==b:
  print("平局")
else:
    print('玩家输了')

# 循环变量
a=0
# 循环条件
while a<5:
    # 循环体
    print("媳妇我错了，说了第%d次" % a)

    # 循环变量发生变化
    a =a+1



n =1
sum =0
while n<=100:
    sum = sum+n
    n+=1
print("sum",sum)


n =0
while n<5:
    print("*",end="")
    n+=1

m =0
while m<=5:
    n =0
    while n<5:
        print("*",end="")
        n+=1

    print("")
    m+=1