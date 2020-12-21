#_*_ coding:utf-8 _*_
#@Time      :2020-11-2214:43
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :列表.py
#@Software:PyCharm


name_list =['xiaoming','Tom','Rose']

print(name_list[0])
print(name_list[1])
print(name_list[2])

print(name_list.index("Tom",0,2))

print(name_list.count("Tom"))
name_list =['xiaoming','Tom','Rose']
print(len(name_list))



name_list =['xiaoming','Tom','Rose']

print("Tom" in name_list)
print("ddd" in name_list)

print("Tom" not in name_list)
print("sd" not in name_list)

# name_list =['xiaoming','Tom','Rose']
# name = input("请输入一个名字：")
#
# if name in name_list:
#     print(f"您输入的名字是{name},名字已经存在")
# else:
#     print(f"您输入的名字是{name},名字不存在")

# 增加
# name_list =['xiaoming','Tom','Rose']
# name_list.append("suahng")
# print(name_list)
# name_list =['xiaoming','Tom','Rose']
# name_list.append(['wangwu','lisi'])
# print(name_list)
# name_list =['xiaoming','Tom','Rose']
# # name_list.extend("suahng")
# # print(name_list)
#
# # name_list.extend(['wangwu','lisi'])
# # print(name_list)
# #
# # name_list.extend(['wangwu','lisi'])
# name_list.insert(1,'wangwu')
# print(name_list)

# 删除


name_list = ['xiaoming','Tom','Rose']
# del name_list
# print(name_list)
#
#
# del name_list[0]
# print(name_list)
#
# # pop()
# del_name= name_list.pop(1)
# print(del_name)
#
# print(name_list)
# name_list = ['xiaoming','Tom','Rose']
# name_list.remove("Tom")
# print(name_list)

# clear()
# name_list.clear()
# print(name_list)


# 修改
name_list = ['xiaoming','Tom','Rose']

name_list[0]="ffd"
print(name_list)


# reverse()
num_list=[1,2,3,45,56]
num_list.reverse()
print(num_list)

num_list=[1,2,3,45,56]
num_list.sort()
print(num_list)

name_list2 = name_list.copy()
print(name_list2)

