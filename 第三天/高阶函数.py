#_*_ coding:utf-8 _*_
#@Time      :2020-12-0617:17
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :高阶函数.py
#@Software:PyCharm


def sum_num(a,b,f):
    return f(a) + f(b)


result = sum_num(-1,2,abs)
print(result)

def sum_num(a,b,f):
    return f(a) + f(b)


result = sum_num(-1,2,round)
print(result)



list1= [1,2,3,4,5]

def func(x):
    return x **2

result =map(func,list1)
print(result)
print(list(result))

#
