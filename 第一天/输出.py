#_*_ coding:utf-8 _*_
#@Time      :2020-11-1514:08
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :输出.py
#@Software:PyCharm


age = 18
name = 'TOM'
weight = 75.3
studengt_id = 1
print('我的名字是%s' % name)

print('我的学号是%4d' % studengt_id)

print('我的体重是%.2f公斤' % weight)

print('我的名字是%s,今年%d岁了' % (name ,age))

print('我的名字是%s,明年%d岁了'% (name,age + 1))

print(f'我的名字是{name},明年{age + 1}岁了')