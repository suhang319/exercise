#_*_ coding:utf-8 _*_
#@Time      :2020-12-2016:36
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :继承.py
#@Software:PyCharm

class Master(object):

    def __init__(self):
        self.kongfu ="[煎饼果子配方]"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(Master):

    pass

# 类的实例化   创建对象
a=Prentice()
print(a.kongfu)
a.make_cake()


# 父类A
class A(object):
    def __init__(self):
        self.num=1

    def info_print(self):
        print(self.num)
# 子类
class B(A):
    pass

result =B()
result.info_print()

class Master(object):
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

class Prentice(Master):
    pass
# 创建对象
xioaming =Prentice()
print(xioaming)

xioaming.make_cake()



# 多继承
# 一个类继承多个父类

class Master(object):
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kmgfu}制作煎饼果子")

# 创建学校类
class School(object):
    def __init__(self):
        self.komgfu ="[香辣煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

class Prentice(School,Master):
    pass
xioaming =Prentice()
print(xioaming.kongfu)
xioaming.make_cake()


# 子类重写父类同名方法和属性

class  Master(object):
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'

    def male_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")


class School(object):
    def __init__(self):
        self.kongfu ='[香辣煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

class Prentice(School,Master):
    def __init__(self):
        self.kongfu='[独家配方]'

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

xiaoming =Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()

print(Prentice.__mro__)



class Washer():

    def __init__(self,width,height):
        self.width=width
        self.height=height
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f"洗衣机的高度是{self.height}")

    def __str__(self):
        return "这是海尔洗衣机说明书"


haier1 =Washer(10,20)
print(haier1)