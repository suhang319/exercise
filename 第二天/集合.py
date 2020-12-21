#_*_ coding:utf-8 _*_
#@Time      :2020-11-2217:22
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :集合.py
#@Software:PyCharm
# 创建集合
s1 ={10,20,30,40,50}
print(s1)

s2={10,20,30,10,20,30}
print(s2)

s3 =set("adcdef")
print(s3)

s4 =set()
print(s4)
s5 ={}
print(type(s5))

s1 ={10,20}
# s1.update(100)
# 增加 .update 和.add
s1.update([100,200])
s1.update("abc")
print(s1)
s1 ={10,20}
s1.add(100)
s1.add(10)
print(s1)

# 删除数据remove()

s1={10,20,}
s1.remove(10)
print(s1)
# s1.remove(10)
print(s1)

s1={10,20,}
s1.discard(10)
print(s1)
s1.discard(10)
print(s1)

s1 ={10,20,30,40}
name= s1.pop()
print(name)
print(s1)
# 查找
s1 ={10,20,30,40}
print(10 in s1)

print(10 not in s1)


print(20 in s1)
print(20 not in s1)

