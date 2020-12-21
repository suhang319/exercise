#_*_ coding:utf-8 _*_
#@Time      :2020-12-0614:48
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :不定长参数.py
#@Software:PyCharm

# 不定长参数也叫可变参数，用于不确定调用的时候传递多少个参数，包裹关键字参数，进行传参
def user_info(*args):
    print(args)


user_info("tom")
user_info('tom',10)
list1=[10,20,30,40]
user_info(*list1)

user_info(" ")

user_info()

user_info()




