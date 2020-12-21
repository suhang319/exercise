#_*_ coding:utf-8 _*_
#@Time      :2020-12-1522:23
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :6.py
#@Software:PyCharm

a=1
print(type(a))

b=1.1
print(type(b))

c =True
print(type(c))

d ="12345"
print(type(d))

e =[10,20,30]
print(type(e))

f =(10,20,30)
print(type(f))

h ={10,20,30}
print(type(h))

g ={'name':"TOM","age":20}
print(type(g))


age=19
name="TOM"
weight=75.5
student_id =1

print("我的名字是%s" % name)
print("我的学号是%4d" % student_id)
print("我的体重是%.2f" % weight)

print("我的名字是%s,今年%d岁了" % (name,age+1))
print(f"我的名字是{name},明年{age+1}岁了")

num =1
print(float(num))
print(type(float(num)))

num2=10
print(type(str(num2)))

str1='10'
str2="[1000,2000,3000]"
str3='(100,200,300)'
print(type(eval(str1)))
print(type(eval(str2)))


# find()检查子串是否在这个字符串中，在返回下标，不在返回-1

#字符串序列.find(子串，开始位置，结束位置)



mystr ="hello world and superctest and chaoge and python "

print(mystr.find('and'))

print(mystr.find('and',16,30))
print(mystr.find("fdsf"))

print(mystr.count('and'))


# 分割 字符串序列.split(分割字符，num)
mystr1 ='hello world and supertest and chaoge and python '

a =mystr1.split("and")
print(a)



# join 字符或者子串.join(多字符串组成的序列)

list=['chao','ge','test','promotion']
t1=('aa','bb','cc','ddd')
print("-".join(list))
print('..'.join(t1))



age =20
if age >=18:
    print("已经成年，可以上网")

age= int(input("请输入您的年龄"))
if age <18:
    print(f'您的年龄是{age},童工一名')

elif age>=18 and age <=60:
    print(f"您的年龄是{age},合适年龄")

elif age >60:
    print(f"您的年龄是{age},可以退休")



money =int(input("请输入您的钱数") )

if money ==1:
    print("有钱，可以上车")

    seat=int(input("输入座位数"))

    if seat ==0:
        print("有座可以坐下")
    else:
        print("没坐")
else:
    print("没钱，走着")


n=1
sum=0

while n<=100:
    sum =sum+n

    n +=1
print("sum",sum)