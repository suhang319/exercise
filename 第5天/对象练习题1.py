#_*_ coding:utf-8 _*_
#@Time      :2020-12-2011:58
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :对象练习题1.py
#@Software:PyCharm

# 打印小猫爱吃鱼，打印小猫要喝水


class Cat():
    def chi(self):

        print(f'小猫爱吃鱼')

    def he(self):

        print(f"小猫要喝水")

xiaomao1=Cat()
xiaomao2=Cat()

xiaomao1.chi()
xiaomao2.he()


class Cat():
    def chi(self,food):
        print(f'小猫爱吃鱼{food}')

    def he(self,wood):
        print(f"小猫要喝水{wood}")


xiaomao1 = Cat()
xiaomao2 = Cat()

xiaomao1.chi('鱼')
xiaomao2.he("水")





# 性别为男的梁超老师教测试


"""""
属性
性别 男
姓名 梁超
方法 教测试
老师 对象
职业  类
"""
class Zhiye():
    def __init__(self,gendre,name):

        self.gender=gendre
        self.name = name
    def jiao(self,jiao):

        print(f"性别为{self.gendre}的{self.name}老师教{jiao}")

teter=Zhiye("男","梁超")
teter.jiao('测试')



