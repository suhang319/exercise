#_*_ coding:utf-8 _*_
#@Time      :2020-12-2016:59
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :子类重写父类.py
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
    def __init__(self):
        self.kongfu='[独创煎饼配方]'
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

# 子类的实例化  创建对象
# 子类和父类具有同名属性和方法，默认使用子类的同名属性和方法
xiao=Prentice()

print(xiao.kongfu)

xiao.make_cake()

print(Prentice.__mro__)