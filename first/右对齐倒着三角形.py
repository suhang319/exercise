#_*_ coding:utf-8 _*_
#@Time      :2020-11-2118:37
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :右对齐倒着三角形.py
#@Software:PyCharm

# *****
#  ****
#   ***
#    **
#     *


"""
a= 1 b =0 c=5
a= 2 b =1 c=4
a= 3 b =2 c=3
a= 4 b =3 c=2
a= 5 b =4 c=1
a是行 b是空格 c是*
a-b=1
b =a-1
"""
a= 0
while a<=5:
    b =0
    while b<=a-1:
        print(" ",end="")
        b+=1
    c =1
    while c<6-a:
        print("*",end="")
        c+=1

    print()
    a+=1
