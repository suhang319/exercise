#_*_ coding:utf-8 _*_
#@Time      :2020-12-0614:36
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :关键字参数.py
#@Software:PyCharm


# 如果有位置参数，位置参数放到关键字参数的前面
def user_info(name,age,gengder):
    print(f'您的名字是{name},年龄是{age},性别是{gengder}')



user_info("xiaoming",age =20,gengder='男')
user_info("小明",gengder="女",age=30)
