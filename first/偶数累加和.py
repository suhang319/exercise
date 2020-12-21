#_*_ coding:utf-8 _*_
#@Time      :2020-11-1723:19
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :偶数累加和.py
#@Software:PyCharm


# i=0
# sum =0
#
# while i<=100:
#     sum = sum +i
#     i +=2
# print(sum)


# i=1
# sum= 0
# while i<=100:
#     if i % 2 == 0:
#         sum = sum +i
#     i+=1
# print(sum)


i = 1
sum= 0

while i<=100:
    if i%2 ==0:
        sum = sum +i
    i +=1
print(sum)
