#_*_ coding:utf-8 _*_
#@Time      :2020-11-2116:31
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :右对齐三角形.py
#@Software:PyCharm

#     *1
#    **2
#   ***3
#  ****4
# *****5

# 5行 第一行4个空格一个星星，第二行3个空格2个星星


'''
a 表示行 b 表示空格
a =1 b =4 c=1
a=2 b =3  c =2
a=3b =2   c =3
a= 4 b =1  c =4
a =5 b =0  c =5
a+b=5 b=5-a  a+b=c c=a-b
'''

a =0
while a<=5:

    b=0
    while b<5-a:
        print(" ",end='')
        b+=1

    c= 0
    while c<a:
        print("*",end="")
        c+=1
    print()
    a+=1