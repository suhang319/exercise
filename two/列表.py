#_*_ coding:utf-8 _*_
#@Time      :2020-11-2421:20
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :列表.py
#@Software:PyCharm

# 列表
name_list =['TOM','liyu','rose']

print(name_list[0])
print(name_list[1])
print(name_list[2])
# index()返回指定的下标 用法 列表序列.index(数据，开始位置，结束位置)
print(name_list.index("liyu"))
print(name_list.index("liyu",0,2))

# count()统计指定数据在当前列表出现次数
name_list =['TOM','liyu','rose']
print(name_list.count("TOM"))

# len()访问列表长度，即列表中数据个数
name_list =['TOM','liyu','rose']
print(len(name_list))

# in 和not in :判断指定数据在某个列表序列，在返回True 否则返回False
name_list =['TOM','liyu','rose']
print("TOM" in name_list)
print("s" in name_list)
print("TOM" not in name_list)
print("sd" not in name_list)

# append()
# 列表序列.append()
name_list =['TOM','liyu','rose']
name_list.append("dfr")
print(name_list)
# 追加的数据是一个序列，追加整个序列到 列表
name_list = ["Tom",'lily','Rose']
name_list.append(["ddd",'xiaoming'])
print(name_list)

# exend()
# 列表结尾追加数据，数据是一个序列，则序列逐一添加到列表
# 列表序列.extend(数据)
name_list = ["Tom",'lily','Rose']
name_list.extend('xiaoming')
print(name_list)
name_list.extend(["ffg",'ffsff'])
print(name_list)

# insert()指定位置新增数据
# 语法 列表序列.insert(位置下标，数据)

name_list = ["Tom",'lily','Rose']
name_list.insert(2,"fgr")
print(name_list)

# del
name_list = ["Tom",'lily','Rose']

# del name_list
#
# print(name_list)

del name_list[0]
print(name_list)

# pop()
# 列表序列.pop(下标）
name_list = ['TOM','LIYU','ROSE']
del_name =name_list.pop(1)
print(name_list)

# remove()移除列表中某个数据的第一个匹配项

# 列表.remove(数据)
name_list = ['TOM','LIYU','ROSE','TOM']
name_list.remove("TOM")
print(name_list)
# clear()清空列表
name_list = ['TOM','LIYU','ROSE','TOM']
name_list.clear()
print(name_list)

# 修改指定的下标路劲
name_list = ['TOM','LIYU','ROSE','TOM']
name_list[0] ='eee'
print(name_list)

# 逆置 reverse()
num_list = [1,4,5,3,6,8]
num_list.reverse()
print(num_list)


# 排序 sort()
# 列表序列.sort(key =None,reverse=False)

num_list = [1,4,5,3,6,8]
num_list.sort()
print(num_list)

# copy
name_list = ['TOM','LIYU','ROSE','TOM']
a =num_list.copy()
print(a)

num_list = ["TOM",'lily','rose']

for i in num_list:
    print(i)