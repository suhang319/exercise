#_*_ coding:utf-8 _*_
#@Time      :2020-12-2615:08
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :练习.py
#@Software:PyCharm


# 定义一个类

class Washer():
    def print_info(self):
        print(f'洗衣机的高度是{self.height}')
        print(f"洗衣机的宽度是{self.width}")

# 创建对象

haier =Washer()

haier.width =100
haier.height=200

haier.print_info()



class Washer():
    def __init__(self):
        self.width=500
        self.height=200
    def print_info(self):
        print(f"洗衣机的宽度是{self.width},高度是{self.height}")

haier1=Washer()
haier.print_info()

class Washer():
    def  __init__(self,width,height):
        self.width=width
        self.height=height

    def print_info(self):
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")


haier1=Washer(10,20)
haier1.print_info()

class Washer():
    def __init__(self,width,height):
        self.width =width
        self.height=height

    def __str__(self):
        return"这是海尔洗衣机的说明书"


haier2=Washer(10,20)
print(haier2)