#_*_ coding:utf-8 _*_
#@Time      :2020-12-0615:05
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :包裹关键字传递.py
#@Software:PyCharm

def user_info(**kwargs):

    print(kwargs)


user_info(name='tom',age=20,gender='男')
dict1={'name':'tom','age':20,'aender':'女'}
user_info(dict1)