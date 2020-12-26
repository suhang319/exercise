# _*_ coding:utf-8 _*_
# @Time      :2020-12-2419:51
# @Author    :lemon_suhang
# @Email  :1147967632@qq.com
# @File   :第5次作业.py
# @Software:PyCharm


# 前提：课上的所有内容复习一遍，检查哪些地方还未理解
#
# Python练习题：
# 提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递
#
# 1、打印小猫爱吃鱼，小猫要喝水
"""
类 猫
方法
吃鱼
喝水

"""


class Cat():
    def eit(self, food):
        print(f"小猫爱吃{food}")

    def dirk(self, wort):
        print(f"小猫爱喝{wort}")


xiao = Cat()
xiao.eit("鱼")
xiao.dirk("水")

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

""""




"""

#
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
#
"""
房子类
属性 ：户型，房子总面积，房子剩余面积
方法：添加家具
家具类
家具名字，占地面积


"""


class Home():
    def __init__(self, area, hu):
        self.area = area
        self.free_area = area
        self.hu = hu
        self.furniturelist = []

    def __str__(self):
        return f'房子的户型是{self.hu},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniturelist}'

    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniturelist.append(item.area)

            self.free_area -= item.area
        else:
            print("家具太大，剩余面积不足，无法容纳")


class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


bed = Furniture('床', 4)
jia1 = Home(1200, "三室二厅")
print(jia1)
jia1.add_furniture(bed)
print(jia1)

wardrobe = Furniture("柜子", 2)
jia1.add_furniture(wardrobe)
print(wardrobe)

table =Furniture("餐桌",1.5)
jia1.add_furniture(table)
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

# 类 士兵
class Soldier():
    def __init__(self,name,have):


        self.name=name
        self.have=have
    def fire(self,a):

        print(f"士兵{self.name}有一把{self.have},可以扣动扳机")
        a.lanunch_bullet(10)
class Gun():
    def __init__(self,bullet=0):
        self.bullet=bullet

    def lanunch_bullet(self,bullet):
        self.bullet += bullet
        if self.bullet>0:
            print(f"发射子弹成功")
    def __str__(self):
        return f"发射成功，剩余子弹数{self.bullet}"
# .format()
    def fill_bullet(self,fill):

        if 0<=self.bullet<50:
            print(f"填充子弹{fill}")

        else:
            print(f"弹夹已满")

ruien=Soldier("瑞恩","AK47")
# ruien.fire(10)
# print(ruien)





qiaong=Gun()
qiaong.lanunch_bullet(4)
print(qiaong)
qiaong=Gun()
qiaong.fill_bullet(5)

ruien.fire(qiaong)



