#_*_ coding:utf-8 _*_
#@Time      :2020-11-1514:41
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :数据转换.py
#@Software:PyCharm


num = input('请输入您的幸运数字：')

print(f'您的幸运数字是{num}')

print(type(num))

print(type(int(num)))


num1 = 1
print((float(num1)))
print((type(float(num1))))

num2= 10
print(type(str(num2)))

list11 = [10,20,30]
print(type(list11))
print(type(tuple(list11)))


t1 =(100,200,300)
print(list(t1))
print(type(list(t1)))

str1 = '10'
str2 = '[1,2,3]'
str3 = '(1000,2000,3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
