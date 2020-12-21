#_*_ coding:utf-8 _*_
#@Time      :2020-11-1821:35
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :打印正三角型.py
#@Software:PyCharm

'''
*
**
***
****
*****
'''


# a =1
# while a<=5:
#     print("*" * a)
#     a +=1




# a =1
# while a<=5:
#     i=1
#     while i<=a:
#         print("*",end="")
#         i+=1
#
#     print("" )
#
#     a+=1

for i in range(6):
    for O in range(0, 5):
        if i>O :
            print("*",end="")


    print("")