#_*_ coding:utf-8 _*_
#@Time      :2020-11-2216:16
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :元组.py
#@Software:PyCharm
t1 =(10,20,30)
print(type(t1))
print(t1)

t2=(20,)
print(t2)
print(type(t2))
t3 =20
print(type(t3))

t4 ="hello"
print(t4)
print(type(t4))


tuple1= ('aa','bb','cc','dd')
print(tuple1[0])

tuple1= ('aa','bb','cc','dd')
print(tuple1.index("aa"))

tuple1= ('aa','bb','cc','dd')
print(len(tuple1))

tuple1 =('aa','bb','cc','dd')
print(tuple1.count("bb"))

# tuple1 =('aa','bb','cc','dd')
# tuple1[0]='aaa'

tuple2=(10,20,['aa','bb','cc',50,30])
tuple2[2][0]='aaaaaaa'
print(tuple2)