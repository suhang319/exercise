#_*_ coding:utf-8 _*_
#@Time      :2020-12-0615:46
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :可变数据.py
#@Software:PyCharm


def test1(a):
    print(a)

    print(id(a))
    a+=a

    print(a)
    print(id(a))

b =100
test1(b)


c =[11,22]
test1(c)