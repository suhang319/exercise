#_*_ coding:utf-8 _*_
#@Time      :2020-12-0611:05
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :函数.py
#@Software:PyCharm


def add_num(a,b):
    result = a+ b
    print(result)




add_num(10,20)

# def dele_func():
#     print("----请选择功能----")
#     print("查询余额")
#     print('存款')
#     print('取款')
#     print("请选择功能")
#
# dele_func()


def duy():
  return "烟"

con=duy()
print(con)

def sum_a(a,b):
    # """求和函数"""
    '''求和函数'''
    return a+b

a=int(input("输入一个数"))
b=int(input("输入一个数"))
s =sum_a(a,b)
print(s)

help(sum_a)


