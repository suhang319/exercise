#_*_ coding:utf-8 _*_
#@Time      :2020-12-2011:32
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :del魔法方法.py
#@Software:PyCharm

class Washer():

    def __init__(self,whigit,hight):


        self.whigit=whigit
        self.hight=hight

    def __del__(self):
        print(f"{self}对象已经被删除")


haier1=Washer(10,20)
del haier1