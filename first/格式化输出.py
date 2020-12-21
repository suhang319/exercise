#_*_ coding:utf-8 _*_
#@Time      :2020-11-1522:39
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :格式化输出.py
#@Software:PyCharm

name = "Tom"
age = 20
weight= 76.5
student_id = 1

# print("我今年%d岁" % age)
#
# print("我的名字是%s" % name)
#
print("我的体重是%.5f" % weight)
# print("我的学号是%4d" % student_id)


print("我今年%d岁,我的名字是%s" % (age,name))

print("我的名字是%s,明年我就%d岁了" % (name,age +1))

print(f"我今年{age+1}岁，我的名字是{name}")