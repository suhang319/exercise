#_*_ coding:utf-8 _*_
#@Time      :2020-11-1515:45
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :条件语句.py
#@Software:PyCharm
# a =1
# if a>0:
#     print("a大于0")
# print('错误')
#
#
# age =20
# if age >=18:
#     print("年龄大于18可以上网")
#
# print("小于18不可以上网")
#
#
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("年龄大于18可以上网")
#
# print("关闭系统")


# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("年龄大于18可以上网")
# else:
#     print(f"您输入的年龄是{age},不可以上网")
# print("关闭系统")


age = int(input("请输入您的年龄："))
if age <18:
    print(f'您输入的年龄是{age}，非法童工')
elif (age>18 and age<60):
    print("合法的工龄")
elif age >60:
    print(f'您输入的年龄是{age}，退休的工龄')
