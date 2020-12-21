#_*_ coding:utf-8 _*_
#@Time      :2020-11-1720:26
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :if语句.py
#@Software:PyCharm

#
# age = int(input("请输入您的年龄："))
#
# if age>=18:
#     print(f"您输入的年龄是{age},满足条件可以上网")
# print("关闭")


# age = int(input("请输入您的年龄："))
# if age>=18:
#     print(f"您输入的年龄是{age},可以上网")
# else:
#     print("不可以上网")
#
# print("退出系统")



age =int(input("请输入您的年龄："))
if age <18:
    print("非法童工，不可以工作")
elif age>18 and age<60:
    print("可以 工作")
elif age>60:
    print("退休")
else:
    print("不用上班")