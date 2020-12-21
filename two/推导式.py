#_*_ coding:utf-8 _*_
#@Time      :2020-11-2921:48
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :推导式.py
#@Software:PyCharm


# 准备一个空列表
list= []
i =0
while i<=10:
    list.append(i)
    i +=1

print(list)

# for 循环
list=[]

for i in range(10):
    list.append(i)
print(list)

# 列表推导式
list1 =[i for i in range(10)]
print(list)


# 创建0-10的偶数列表
list1 =[i for i in range(0,10,2)]
print(list1)

list2=[i for i in range(10) if i %2==0]
print(list2)
# 俩个列表河滨成为一个字典
list3=['name','age','gender']
list4=['tom',20,'man']
dict1={list3[i]:list4[i] for i in range(len(list4))}
print(dict1)
# key是1-5的数，value是这个数字的二次方
dict1 ={i :i**2 for i in range(1,5)}
print(dict1)

counts={'mbp':386,"HP":125,"DEL":201,'lenovo':199,'acer':99}
count1 ={key: value for key,value in counts.items() if value>=200 }
print(count1)

list1 =[1,1,2]
set1={i ** 2 for i in list1}
print(set1)