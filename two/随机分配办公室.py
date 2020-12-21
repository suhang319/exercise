#_*_ coding:utf-8 _*_
#@Time      :2020-11-2423:02
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :随机分配办公室.py
#@Software:PyCharm

# 有三个办公室，8位老师，8位老师随机分配到3个办公室

import random

lit1=[[],[],[]]
lit2=['1','2','3','4','5','6','7','8']
for i in lit2:
    a = random.randint(0,2)
    lit1[a].append(i)
print(lit1)