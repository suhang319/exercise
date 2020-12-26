#_*_ coding:utf-8 _*_
#@Time      :2020-12-2018:50
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :静态方法.py
#@Software:PyCharm


class Dog(object):
    @staticmethod
    def info_print():
        print("这是一个狗类，用于创建狗实例")


wangcai =Dog()

wangcai.info_print()
Dog.info_print()

wangcai.info_print()