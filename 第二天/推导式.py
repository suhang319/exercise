#_*_ coding:utf-8 _*_
#@Time      :2020-11-2218:28
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :推导式.py
#@Software:PyCharm


list =[]
i= 0

while i <=10:
    list.append(i)
    i+=1
    print(list)




list1 =[]
for i in range(10):
    list1.append(i)
    print(list1)

#   推导式
list2 =[i for i in range(10)]
print(list2)

# 嵌套循环
list1 =[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]


for i in range(1,3):
    for j in range(3):
        print((i,j))


# 字典推导式

dict1 = {i:i**2 for i in range(1,5)}
print(dict1)


list1 = ['name','age','gender']
list2 = ['Tom','20','man']
dict1= {list1[i]:list2[i] for i in range(len(list1))}
print(dict1)

count = {"MBP":269,'HP':123,'DELL':201,"Lenovo":199,'acer':99}

count1= {key:  value for key, value in count.items() if value >= 200}
print(count1)