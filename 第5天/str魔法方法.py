#_*_ coding:utf-8 _*_
#@Time      :2020-12-2011:27
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :str魔法方法.py
#@Software:PyCharm


class Washer():


    def __init__(self,width,hight):
        self.width=width
        self.hight=hight

    def __str__(self):

        return "这是海尔洗衣机说明书"


haier = Washer(10,20)
print(haier)
