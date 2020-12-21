#_*_ coding:utf-8 _*_
#@Time      :2020-11-1922:16
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :lianmxi.py
#@Software:PyCharm

age =18
name ="tmo"
weight =78.4
student_id =1
print("我的名字是%s" % name)
print("我的学号是%4d" % student_id)
print("我的体重是%.2f公斤" %weight)
print("我的名字是%s,我今年%d岁了" % (name,age))
print("明年我%d岁了" % (age+1))
print(f"我今年{age}岁")
# 换行\n
# \t:制表符 1个tab建4个空格

password = input("请输入您的密码：")
print(f"您输入的密码是{password}")
print(type(password))


num = input("请输入一个数：")
print(f"您输入的幸运数字是{num}")
print(type(num))
print(type(int(num)))

num1=1
print(float(num))
print(type(float(num1)))

num2=10
print(type(str(num)))

list1 = [10,20,30]
print(list(list1))
print(type(list(list1)))


t1=(100,200,300)
print(list(t1))
print(type(list(t1)))

str = "10"
a = "[1,2,3]"
b =(10,20,30)

print(type(eval(str)))
print(type(eval(a)))
print(type(eval(b)))


if True:
    print("条件成立的代码")
print("无论如何都执行")

age=20
if age>=18:
     print("可以上网")
print("系统关闭")

age =int(input("请输入您的年龄："))
if age >= 18:
        print("可以上网")
print("系统关闭")

age =int(input("请输入您的年龄："))
if age <18:
    print("非法童工，不可以工作")
elif age>18 and age<60:
    print("可以 工作")
elif age>60:
    print("退休")
else:
    print("不用上班")


