#_*_ coding:utf-8 _*_
#@Time      :2020-12-2018:31
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :类属性.py
#@Software:PyCharm

# 类属性
class Dog(object):
    tooth =10



wangcai =Dog()
xioahei =Dog()

print(Dog.tooth)
print(wangcai.tooth)
print(xioahei.tooth)


# 修改类属性

class Dog(object):
    tooth=10

wangcai =Dog()
xioahei=Dog()


# 修改类属性
Dog.tooth=12
print(Dog.tooth)
print(wangcai.tooth)
print(xioahei.tooth)

wangcai.tooth =20
print(Dog.tooth)
print(wangcai.tooth)
print(xioahei.tooth)


# 实例属性

class Dog(object):
    def __init__(self):
        self.age=5


    def info_print(self):
        print(self.age)


wangcai =Dog()
print(wangcai.age)

wangcai.info_print()





