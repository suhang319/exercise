#_*_ coding:utf-8 _*_
#@Time      :2020-11-2214:04
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :练习.py
#@Software:PyCharm


name= input("从键盘输入一个名字：")

vipname='laingchao suhang xiaoming gaoweijian xiaoming'


if (vipname.find(name))!= -1:


    if (vipname.count(name)) >1:
        print(f"有重名,重名的个数{vipname.count(name)}")

    else:
        print("在，无重名")
else:
    print("不在班级内")

