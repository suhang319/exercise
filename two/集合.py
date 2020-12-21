#_*_ coding:utf-8 _*_
#@Time      :2020-11-2619:48
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :集合.py
#@Software:PyCharm

# 创建空集合set()

s1= {10,20,30,40}
print(s1)

# 集合可以去掉重复数据 ，集合是无序的，不支持下标

s2 = {10,20,20,20,30,30,40,40,50}
print(s2)

s3 =set('gfdffd')
print(s3)

# 增加 add()
s1 ={10,20}
s1.add(100)
s1.add(10)
print(s1)

#
# update()
s1 ={10,20}
s1.update([100,200])
s1.update('abs')
print(s1)



# 删除

# remove() 删除集合中指定数据，如果不存在则报错
s1={10,20}
s1.remove(10)
print(s1)


# s1.remove(10)
# print(s1)

# discard() 删除集合中指定数据，不存在不会报错

s1 ={10,20}
s1.discard(10)
print(s1)
s1.discard(10)
print(s1)

# pop()随机删除集合中的某个数据，并返回这个数据
s1 ={10,20,30,40}
del_num =s1.pop()
print(del_num)
print(s1)

# 查找数据
s1 ={10,20,30,40}

print(10 in s1)
print(10 not in s1)

