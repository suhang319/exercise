#_*_ coding:utf-8 _*_
#@Time      :2020-11-2216:48
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :字典.py
#@Software:PyCharm

dict1= {"name":'Tom','age':'20','gender':"男"}

# 空字典
dict2={}
dict3 =dict()
# 增加
dict1= {"name":'Tom','age':'20','gender':"男"}

dict1['name']= 'Rose'

print(dict1)

dict1['id']=110
print(dict1)

# 删除

dict1= {"name":'Tom','age':'20','gender':"男"}
# del dict1

del dict1['gender']
print(dict1)


dict1= {"name":'Tom','age':'20','gender':"男"}
dict1.clear()
print(dict1)

# 改
dict1= {"name":'Tom','age':'20','gender':"男"}
dict1['name']="su"
print(dict1)
dict1= {"name":'Tom','age':'20','gender':"男"}
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))

# keys
dict1= {"name":'Tom','age':'20','gender':"男"}
print(dict1.keys())
# values
dict1= {"name":'Tom','age':'20','gender':"男"}
print(dict1.values())

dict1= {"name":'Tom','age':'20','gender':"男"}
print(dict1.items())

dict1= {"name":'Tom','age':'20','gender':"男"}
print()


dict1= {"name":'Tom','age':'20','gender':"男"}
for key in dict1.keys():
    print(key)

dict1= {"name":'Tom','age':'20','gender':"男"}
for value in dict1.values():
    print(value)

dict1= {"name":'Tom','age':'20','gender':"男"}
for item in dict1.items():
    print(item)

dict1= {"name":'Tom','age':'20','gender':"男"}
for key,value in dict1.items():
    print(f"{key} = {value}")
