#_*_ coding:utf-8 _*_
#@Time      :2020-11-1515:16
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :运算符.py
#@Software:PyCharm

a = 0
b = 1
c = 2
# and运算符，只要一个为0，则结果为0，否则结果为最后一个非0数字
print(a and b )
print(b and c)
print(a and c)
print(c and a)
print(b and c)
print(c and b)

# or运算符，只有所有结果都为0，才为0，否则第一个非0数字
print(a or b)
print(a or c)
print(b or b)


a = 1
b = 2
c = 3

print((a<b) and (b<c))
print((a>b) and (b<c))
print((a>b) or (b<c))
print((a>c) and (b>c))
print((b<c) and (a>c))
print(not(a>b))
print(not(a<b))

print((c<a) or (a>b))
