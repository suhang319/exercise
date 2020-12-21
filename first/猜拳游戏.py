#_*_ coding:utf-8 _*_
#@Time      :2020-11-1721:05
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :猜拳游戏.py
#@Software:PyCharm

'''
player 代表玩家
computer 电脑
石头=0
剪刀=1
布=2

'''

import random

compuuter = random.randint(0,2)
print(compuuter)
player = int(input("请出 0 石头 1剪刀 2布："))

if ((player==0 and compuuter==1)) or ((player==1 and compuuter==2)) or ((player==2 and compuuter==0)):
    print("玩家胜利")

elif player==compuuter:
    print("平局")
else:
    print("玩家输了")



