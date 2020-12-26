#_*_ coding:utf-8 _*_
#@Time      :2020-12-2010:28
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :类的创建.py
#@Software:PyCharm

# 创建类
# class是关键字  类名
class Washer():
    def Wash(self):
        print("洗衣服")
# 空类
class A():
    pass

# 创建对象
# 对象也叫实例
# 类下面可以创建多个对象
haier1=Washer()
ximenzi=Washer()

print(haier1)
print(ximenzi)
# 对象调用方法  互不影响
haier1.Wash()
ximenzi.Wash()