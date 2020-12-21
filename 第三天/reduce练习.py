#_*_ coding:utf-8 _*_
#@Time      :2020-12-0617:33
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :reduce练习.py
#@Software:PyCharm

# reduce用法
import functools

list1 =[1,2,3,4,5]

def func(a,b):
    return a+b

result = functools.reduce(func,list1)

print(result)