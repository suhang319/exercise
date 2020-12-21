#_*_ coding:utf-8 _*_
#@Time      :2020-11-2520:06
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :元组.py
#@Software:PyCharm

t1 =(10,20,30)

t2=(10,)
print(type(t1))
print(type(t2))

te =("helll")
print(type(te))
# 元组不支持修改 只支持查找
tuple =('aa','bb','cc','bb')
print(tuple[0])

# index()用法
tuple =('aa','bb','cc','bb')
print(tuple.index('aa'))

# count()统计数据在元组出现的次数
tuple1 = ('aa','bb',"bb")
print(tuple1.count("bb"))

# len()统计元组中数据的个数
tuple1=("aa",'bb','cc','bb')
print(len(tuple1))

# 元组里边有列表，修改列表的数据是支持的
tuple2 = (10,20,["aa",'bb','cc'])
print(tuple2[2])
tuple1[2][0]= 'ddddd'
print(tuple2)