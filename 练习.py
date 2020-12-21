#_*_ coding:utf-8 _*_
#@Time      :2020-12-1311:01
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :练习.py
#@Software:PyCharm


list = [3,2,1,5,4,0,2]
list1=[]
for i in list:
    i = i **2
    list.append(i)
    print(list1)

list2 = [3,2,1,5,4,0,2]
set1 ={i ** 2 for i in list2}
print(set1)