#_*_ coding:utf-8 _*_
#@Time      :2020-12-0614:10
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :全局和局部变量.py
#@Software:PyCharm


def st():
    a=200
    print(a)

st()


a =110
def rt():
    print(a)
def ry():
    print(a)

rt()
ry()


a =200

def fr():
    print(a)


def vf():
    a =100
    print(a)
fr()
vf()

a =300
def yu():
    print(a)

def pol():

    global a
    a = 440
    print(a)

def pp():
    print(a)

yu()
pol()
pp()


print(f"全局变量a={a}")


# 定义一个全局变量
glo_num =0

def tet1():
    #     修改全局变量
    global glo_num
    glo_num = 100

def test2():
    #     调用test1函数修改
    print(glo_num)


tet1()
test2()


def test1():
    return  50

def test2(num):
    print(num)



result = test1()
test2(result)