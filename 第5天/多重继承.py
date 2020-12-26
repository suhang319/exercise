#_*_ coding:utf-8 _*_
#@Time      :2020-12-2016:46
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :多重继承.py
#@Software:PyCharm


class Master():
    def __init__(self):
        self.kongfu='[五香煎饼果子]'

    def make_cake(self):
        print(f"运用{self.kong}制作")


class School():
    def __init__(self):
        self.kongfu = '[五香煎饼果子]'

    def make_cake(self):
        print(f"运用{self.kong}制作")
# 继承多个父类 ，先查第一个父类，默认使用第一个
class Prentice(School,Master):
    pass

# 子类的实例化  创建对象
xiao=Prentice()

print(xiao.kongfu)

xiao.make_cake()