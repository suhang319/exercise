#_*_ coding:utf-8 _*_
#@Time      :2020-12-2017:31
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :私有权限.py
#@Software:PyCharm


class Master(object):
    def __init__(self):
        self.kongfu ='[五香味煎饼果子]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作")


class School():
    def __init__(self):
        self.kongfu='[黑马煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class Prentice(School,Master):
    def __init__(self):
        self.kongfu="[独创煎饼果子配方]"

        self.__money = 200000


    def __info_print(self):
        print()

