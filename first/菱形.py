#_*_ coding:utf-8 _*_
#@Time      :2020-11-2117:12
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :菱形.py
#@Software:PyCharm
'''

1111*
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
行 a =1 b=4  c=1
行 a =2 b=3  c=3
行 a =3 b=2  c =5
行 a =4 b=1  c =7
行 a =5 b=0  c =9


a = 1  b=1  c=7
a = 2 b=2  c=5
a = 3  b=3  c=3
a = 4  b=4  c=1
i = 7
wh
分析:左上和左下部分的空白，实际上是打印成空格
'''

r=0
while r<=5:
    e=0
    while e<=r:
        print("!",end="")
        e+=1
    p =0
    while p<5:

        i =7
        while i>0:
            if i%2==1:
                print("*"*i,end="")
                i=i-1

        p+=1
        print()



    print()
    r+=1





# 上半部分
# a =0
# while a<=6:
#     b =0
#     while b<6-a:
#         print(" ",end="")
#         b+=1
#
#     c=1
#     while c<=(2*a-1):
#         print("*",end="")
#         c+=1
#
#
#     print()
#     a+=1
#
# r=0
# while r<=5:
#     e=0
#     while e<=r:
#         print("!",end="")
#         e+=1
#
#     t=7
#     while t<=0:
#         if t%2==1:
#             print(t*"*",end="")
#
#             t-=1
#
#     print()
#     r+=1
#
#
#
#












'''''''''
i = 0
while i < 9: # 总循环次数 9
    if i < 5:
        # 上空格部分
        j = 0
        while j < 4 - i:
            print(" ",end="")
            j +=1
        #上部分
        j = 0
        while j < i+1:
            print("*", end=" ")
            j +=1
    else:
    #     # 下空格部分
        j = 0
        while j < i -4:
            print(" ",end="")
            j +=1
    #     # 下部分
        j = 0
        while j < 9 - i:
            print("*",end=" ")
            j  +=1
    print()
    i += 1
    
'''''''''