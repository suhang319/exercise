#_*_ coding:utf-8 _*_
#@Time      :2020-12-0613:43
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :三个数的平均和.py
#@Software:PyCharm


def num(a,b,c):
    return a+b+c


# num()

def avg(a,b,c):
    # 求和
    num_a = num(a,b,c)
    # 除3
    return  num_a/3
# print(avg(1,2,3))
h = avg(1,2,3)
print(h)