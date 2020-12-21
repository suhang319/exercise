#_*_ coding:utf-8 _*_
#@Time      :2020-12-0722:43
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :函数.py
#@Software:PyCharm

# def add_num():
#     result = 1+ 2
#     print(result)
#
# add_num()
#
#
# def add_num2(a,b):
#     result = a+b
#     print(result)
#
# add_num2(10,20)
#
#
# def buy():
#     return  "烟"
# goods = buy()
# print(goods)


# def sum_num(a,b):
#     """求和函数"""
#     return a+b
#
# result = sum_num(1,2)
# print(result)
# help(sum_num)
#
# def testB():
#     print('---这是testB函数的执行代码---')
#
# def testA():
#     print("fdffff")
#     testB()
# testA()
#
#
# def print_line():
#     print("_" * 20)
#
# print_line()
#
# def print_lines(num):
#     i =0
#     while i < num:
#         print_line()
#         i+=1
# print_lines(5)
#
# def sum_num(a,b,c):
#     return a+b+c
#
#
# result = sum_num(1,2,3)
# print(result)

# def avg_num(a,b,c):
#     a = sum_num(a,b,c)
#     return a/3
#
# result =avg_num(1,2,3)
# print(result)



def testa():

    a =100
    print(a)

testa()
# print(a)


def test1():
    return 50

def test2(num):
    print(num)

result=test1()
test2(result)


# 位置参数

def user_info(name,age,gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

user_info('tom',20,'男')

# 关键字参数
def user_info(name,age,gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")
user_info('rose',age=20,genser='女')
user_info('小明',gender='男',age=16)

# 关键字参数

def user_info(name,age,genser):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

user_info("rose",age=20,gender='女')
user_info("小明",gender="男",age=16)

# 缺省参数
def user_info(name,age,gender='男'):
    print(f'您的名字是{name},年龄是{age},性别是{genser}')
user_info('tom',20)
user_info('tom',18,'女')

# 不定长  包裹位置传递

def user_info(*args):
    print(args)

user_info('tom')

user_info('tom',18)
# 根据传递的参数和成一个元组

# 包裹关键字传递
def user_info(**kwargs):
    print(kwargs)


user_info(name="tom",age=18,id=110)


# 拆包
# 元组
def return_num():
    return 100,200

num1,num2 = return_num()
print(num1)
print(num2)


# 拆包：字典
dict1={'name':'tom','age':19}

a,b=dict1
print(a)
print(b)

print(dict1[a])
print(dict1[b])


a =1
b =a
print(b)

print(id(a))
print(id(b))

a =2
print(b)
print(id(a))
print(id(b))

aa =[10,20]
bb=aa

print(id(aa))
print(id(bb))


aa.append(30)
print(bb)

print(id(aa))
print(id(bb))


num=1
print(num)


age =int(input('请输入您的年龄：'))


if age >=18:
    print(f"您的年龄是{age},已经成年，可以上网")

else:
    print(f"您的年龄是{age},weicehgnnia")


    i =0

while i <5:
    print("媳妇，我错了")
    i+=1

def test1(a):
    print(a)
    print(id(a))

    a +=a

    print(a)
    print(id(a))


b =100
test1(b)

c =[11,22]
test1(c)

def print_info():
    print(" "*20)
    print("登录学院管理系统")
    print("1:添加学员")
    print('2:删除学员')
    print("3:修改学员信息")
    print("4:查询学员信息")
    print("5:显示所有学员信息")
    print("-"* 20)
print_info()






