#_*_ coding:utf-8 _*_
#@Time      :2020-12-0616:23
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :lambda练习.py
#@Software:PyCharm

def fn1():
    return  200

print(fn1())
print(type(fn1))

fn2 =lambda :200
print(fn2)
print(fn2())


result = lambda a,b :a+b
# print(resul 1,2))

fn1 =lambda a,b:a if a>b else b
print(fn1(1000,500,))



students= [ {'name':'tom','age':20},

{'name':'rose','age':19},
{'name':'rose','age':21}]

students.sort(key=lambda  x:x['name'])
print(students)

students.sort(key=lambda  x:x['name'],reverse=True)
print(students)

students.sort(key=lambda  x:x['age'])
print(students)
