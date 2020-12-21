#_*_ coding:utf-8 _*_
#@Time      :2020-12-0614:45
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :缺省参数.py
#@Software:PyCharm

# 缺省参数可以不传，默认值
def user_info(name,age,gender='男'):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")



user_info("tom",20)

user_info("tom",21,'女')