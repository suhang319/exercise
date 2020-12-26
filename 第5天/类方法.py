#_*_ coding:utf-8 _*_
#@Time      :2020-12-2018:48
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :类方法.py
#@Software:PyCharm

class Dog(object):
    __tooth=10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


wangcai =Dog()
result =wangcai.get_tooth()
print(result)