#_*_ coding:utf-8 _*_
#@Time      :2020-11-2520:51
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :字典.py
#@Software:PyCharm


# 空字典
dict2 ={}
# 有数据的字典
dict1 = {'name':'Tom','age':20,'gender':'男'}
# 键  key 值 value
# 字典为可变类型

dict1 = {'name':'Tom','age':20,'gender':'男'}
dict1['name']='rose'
print(dict1)
# 字典序列[key]=值

dict1['id']=100
print(dict1)

# 删除
dict1 = {'name':'tom','age':20,'gender':'男'}

del dict1['gender']
print(dict1)
dict1 = {'name':'tom','age':20,'gender':'男'}
dict1.clear()
print(dict1)

# 改  字典序列[key]=值
dict1 = {'name':'tom','age':20,'gender':'男'}
dict1['name']='sdjdjjsd'
print(dict1)


# 查
dict2 ={'name':'fjj','age':40,'gender':'男'}
print(dict1['name'])
# print(dict1["id"])

# get()
# 字典序列.get(key,默认值)

dict2= {'name':'fjjf','age':20,'gender':'男'}
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))


# keys()
dict2= {'name':'fjjf','age':20,'gender':'男'}
print(dict2.keys())

# values()
dict2 = {'name':'tom','age':20,'gender':"男"}
print(dict2.values())

# items()

dict1 ={'name':"df",'age':30,'gender':'男'}
print(dict1.items())


# 字典的循环

dict = {'name':'tom','age':20,'gender':"男"}

for key in dict.keys():
    print(key)

dict = {'name': 'tom', 'age': 20, 'gender': "男"}
for value in dict.values():
    print(value)

dict = {'name': 'tom', 'age': 20, 'gender': "男"}
for key,value in dict.items():
    print(f"{key}={value}")