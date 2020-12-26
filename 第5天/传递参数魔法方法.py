#_*_ coding:utf-8 _*_
#@Time      :2020-12-2011:18
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :传递参数魔法方法.py
#@Software:PyCharm


class Washer():
    def __init__(self,weight,hight):

        self.weight=weight
        self.hight=hight

    def pro_w(self):
        print(f"洗衣机的长度是{self.hight},宽度是{self.weight}")


haier1=Washer(10,20)
haier1.pro_w()
