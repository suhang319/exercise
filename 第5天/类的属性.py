#_*_ coding:utf-8 _*_
#@Time      :2020-12-2010:53
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :类的属性.py
#@Software:PyCharm


# 创建类
class Washer():
    def Wash(self):
        print("洗衣服")

# 创建对象
haier1=Washer()

# 创建类的对象属性
haier1.width=100
haier1.height=200

# 打印属性,获取对象属性
print(f'洗衣机的宽度是{haier1.width}')
print(f"洗衣机的高度是{haier1.height}")
