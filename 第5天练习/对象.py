#_*_ coding:utf-8 _*_
#@Time      :2020-12-2120:58
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :对象.py
#@Software:PyCharm


# 定义一个类

class Washer():
    def wash(self):
        print("我会洗衣服")

# 定义一个空类
class A():
    def B(self):
        pass


# 创建对象 类的实例化

# 对象名 = 类名()

haier1 =Washer()
print(haier1)
# 对象调用实例方法
haier1.wash()


# self 指的是调用该函数的对象
class Washer():
    def wash(self):
        print("我会洗衣服")
        print(self)

# 创建对象
haier2=Washer()
print(haier2)
# 对象调用实例方法
haier2.wash()

haier3=Washer()
haier3.wash()
print(haier3)


# 类的外面添加对象属性
# 对象名.属性名 =值

haier1.width =100
haier1.height=200

print(f"洗衣机宽度{haier1.width}")
print(f"洗衣机长度是{haier1.height}")

# 类里面获取对象属性

# self.属性名


class Washer():
    def print_info(self):
        print(f"洗衣机宽度是{haier1.width}")
        print(f"洗衣机的长度是{haier1.hight}")


# 创建对象

haier1 =Washer()


haier1.width=100
haier1.height=200

haier1.print_info()


# __init__方法的作用 ：初始化对象

class Washer():
    # 定义初始化功能函数
    def __init__(self):
        # 添加实例属性
        self.width=200
        self.height=300

    def print_info(self):
        # 类里边调用实例属性
        print(f"洗衣机的宽度是{self.width},长度是{self.height}")


haier1=Washer()
haier1.print_info()


# 带参数的__init__()

class Washer():
    def __init__(self,width,height):
        self.width=width
        self.hight=height
    def print_info(self):
        print(f"洗衣机宽度是{self.width}")
        print(f"洗衣机的高度是{self.hight}")


haier1=Washer()
haier1.print_info()



# __str__
# 当使用print输出对象，默认打印对象内存地址

class Washer():
    def __init__(self,width,hight):
        self.width=width
        self.hight=hight
    def __str__(self):
        return "这是海尔的洗衣机说明书"
haier1=Washer(10,20)
print(haier1)

# __del__()
class Washer():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def __def__(self):
        print(f"{self}对象已经被删除")


haier1= Washer(10,20)

del haier1






