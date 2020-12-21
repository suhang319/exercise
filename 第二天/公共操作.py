#_*_ coding:utf-8 _*_
#@Time      :2020-11-2218:12
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :公共操作.py
#@Software:PyCharm

# 字符串拼接

str1 ='aa'
str2= 'bb'
str3 =str1 + str2
print(str3)

list =[1,3]
list1=[10,20]
list3=list1+list
print(list3)

t1 =(1,2)
t2 =(10,20)
t3 =t1+t2
print(t3)


print("1"*10)

list =["hello"]
print(list*4)

t1 =('world')
print(t1* 4)


# len()
str= "adafsds"
print(len(str))

list1 =[10,20,30,40]
print(len(list1))

t1 =(10,20,30)
print(len(t1))

s1 = {10,20,30}
print(len(s1))

dict1 ={'name':"Tom","age":"20"}
print(len(dict1))

# del
str1 ="afkdsfk"
del str1
print(str1)

list1 =[10,20]