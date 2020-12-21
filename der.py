#_*_ coding:utf-8 _*_
#@Time      :2020-12-0923:17
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :der.py
#@Software:PyCharm


def sum_numbers(num):
    if num ==1:
        return 1

    return  num + sum_numbers(num-1)


sum_result =sum_numbers(3)
print(sum_result)


def add(a,b):
    return a+b
result =add(1,2)
print(result)


fn1 =lambda a,b:a+b
print(fn1(1,2))

if True:
    print("条件成立执行 的代码")

age=20
if age >=18:
    print("可以上网")

print("不可以上网")


age= input("请输入您的年龄")


if age >=18:
    print(f"您输入年龄是{age},已经成年，可以上网")

else:
    print(f"您的年龄未成功年{age},请回家")

print("系统关闭")


money = 1
if money ==1:
    print("土豪，")
else:
    print("没钱，不能上车")



money =1
seat =0

if money ==1:
    print("可以上车")
    if seat==1:
        print("有座")
    else:
        print("没有空座")
else:
    print("没钱，不可以上车")



import random

computer = random.randint(0,2)
print(computer)
player = int(input("请出 石头0，1是剪刀，2是布"))
if ((player==0) and(computer==1) or (player==1) and(computer==2) or (player==2) and(computer==0)):
    print("玩家胜利")
elif player == computer:
    print("pingju ")
else:
    print('电脑获胜')


a=1
b =2
c =a if a>b else b
print(c)


i =0
while i<5:
    print("媳妇儿，我错了")

    i+=1
print("任务结束")

i=1
result =0
while i <=100:
    result +=i
    i +=1
print(result)



i =1
result =0
while i <=100:
    if i % 2==0:
        result +=i

    i +=1
print(result)


i =1
while i <=5:
    if i ==3:
        print("dachonzi")
        i +=1
        continue
    print("fds")
    i +=1


