#_*_ coding:utf-8 _*_
#@Time      :2020-12-2014:56
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :搬家具.py
#@Software:PyCharm


''''

类
房子
家具

属性
房子总面积
房子的剩余面积
家具列表
户型
方法：



家具的占地面积
家具名称

方法 :无
'''

class Hohms():
    def __init__(self,area,openi):
        self.openi=openi
        self.totalarea=area
        self.area=area
        self.furniture=[]

    def add_Furniture(self,item):
        if self.area >=item.zhan:
            self.furniture.append(item.chen)

            self.area -= self.totalarea

        else:
            print("家具大，放不进去")


class Furniture():
    def __init__(self,chen,zhan):
        self.chen=chen
        self.zhan=zhan

bed =Furniture('床',6)
jia= Hohms(1200,120)
print(jia)

jia.add_Furniture(bed)
print(jia)

