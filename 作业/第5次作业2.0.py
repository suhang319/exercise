# _*_ coding:utf-8 _*_
# @Time      :2020-12-2921:51
# @Author    :lemon_suhang
# @Email  :1147967632@qq.com
# @File   :2.py
# @Software:PyCharm

# 1.小猫爱吃鱼，小猫要喝水

class Cat():

    def eat(self, food):
        print(f"小猫爱吃{food}")

    def he(self, shui):
        print(f"小猫爱喝{shui}")


xiao = Cat()
xiao.eat('鱼')
xiao.he('水')

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

""""
类 人
方法 跑步  吃东西
属性 名字 体重
跑步 减肥0.5公斤
吃东西  增加1公斤



"""


class Persion():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return ('%s的体重是%0.1f公斤' % (self.name, self.weight))

    def run(self):
        self.weight -= 0.5
        print('%s会减肥0.5公斤' % (self.name))

    def eat(self):
        self.weight += 1
        print("%s会增重1公斤" % (self.weight))


a = Persion("小明", 75)

a.run()
a.eat()
print(a)

a1 = Persion("小美", 45)
a1.eat()
a1.run()
print(a1)

# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
类  房子 家具

房子 属性 
总面积  家具列表  剩余面积

家具属性

名字  占地面积

方法；
添加家具




"""


class Home():
    def __init__(self, hu, area):
        self.area = area
        self.flee_area = area
        self.hu = hu
        self.furniturelist = []


    def __str__(self):
         return f'房子的户型是{self.hu},占地面积{self.area},剩余面积{self.flee_area},家具有{self.furniturelist}'


    def add_furniture(self, item):
        if self.flee_area >= item.area:
            self.furniturelist.append(item.area)
            self.flee_area -= item.area
        else:
            print("家具太大，放不下")





class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


bed = Furniture("床",4)
jia =Home("三室二厅",1200)
print(jia)
jia.add_furniture(bed)
print(jia)

wardrobe = Furniture("柜子", 2)
jia.add_furniture(wardrobe)
print(wardrobe)

table =Furniture("餐桌",1.5)
jia.add_furniture(table)
print(table)

# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
''''
需求分析：
类 士兵 
属性  有个枪 AK47
方法 开火

枪类
属性 无
方法 1.发射子弹

2.填充子弹

'''



class Soilder:
    def __init__(self,name):
        self.name =name
    def fire(self,item):
        if item.bullet_count >0:
            print("射击")
            item.shot()
        else:
            print('%s子弹不足' % item.name)
            item.add_bullet()


class Gun():
    def __init__(self,name):
        self.name =name
        self.bullet_count=0

    def add_bullet(self):
        self.bullet_count +=20
        print("%d发子弹填充完毕"%self.bullet_count)

    def __str__(self):
        return "制造一把%s有%d发子弹" % (self.name,self.bullet_count)
    def shot(self):
        self.bullet_count -=1
        print('发射1发，还剩%d发'% self.bullet_count)


AK =Gun("AK47")
AK.add_bullet()
AK.shot()
print(AK.bullet_count)
print(AK.name)
s =Soilder('瑞恩')
s.fire(AK)

