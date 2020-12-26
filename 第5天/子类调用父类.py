#_*_ coding:utf-8 _*_
#@Time      :2020-12-2017:10
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :子类调用父类.py
#@Software:PyCharm


class Master():
    def __init__(self):
        self.kongfu="[五香煎饼果子]"

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

class School():
    def __init__(self):
        self.kongfu='[香辣煎饼果子]'

    def make_cake(self):
        print(f"运用是{self.kongfu}制作")
class Prentice(School,Master):
    def __init__(self):
        self.kongfu='[独创煎饼果子]'
    def make_cake(self):

        self.__init__()
        print(f"运用{self.kongfu制作}")

