#_*_ coding:utf-8 _*_
#@Time      :2020-12-0615:32
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :交换变量值.py
#@Software:PyCharm

a=10
b =20
c=0
c = a

a = b

b =c
print(a)
print(b)


a,b =1,2
a,b =b,a
print(a)
print(b)