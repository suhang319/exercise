#_*_ coding:utf-8 _*_
#@Time      :2020-11-1919:59
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :倒三角.py
#@Software:PyCharm


# a= 0
#
# while a<5:
#
#     i = 0
#     while i< 5:
#         print("*",end ="")
#         i+=1
#
#     print()
#     a+=1


# p=0
# while p<=5:
#     i = 0
#     while i<p:
#         print("*",end="")
#         i+=1
#
#     print()
#     p+=1

# *****
# ****
# ***
# **
# *
# 控制行
# for i in range(6):
# # 控制*号
#     for j in range(6):
#         if i<j:
#             print('*',end="")
#     print("")

# 第2种
# for x in range(5):
#     for i in range(x, 5):
#         print('*', end='')
#     print('')
i = 5
while i > 0:
    # 内循环
    j = 0
    while j < i :
        print("*",end=" ")
        j +=1
    print()
    i -= 1