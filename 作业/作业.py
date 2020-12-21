#_*_ coding:utf-8 _*_
#@Time      :2020-12-1920:21
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :作业.py
#@Software:PyCharm

# 1.5层打印，外层循环 m=5 m=1
# 内层循环控制个数你n<=m

m=1
while m<=5:
    n=1
    while n<=m:
        print("*",end='')
        n +=1
    print()
    m +=1


# 字符串去重
#

str1 ="aabbbcddef"
str2=''
for i in str1:
    if str1.count(i)==1:
        str2+=i
    print(str2)

# 100被3整除的数
list =[]
for i in range(1,101):
    if i % 3 ==0:
        list.append(i)
    print(list)

# 列表去重 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，
# 得到一个唯一元素的列表
list =[1,2,3,4,3,4,2,5,5,8,9,7]
list2=[]

for i in list:
    if i not in list2:
        list2.append(i)
    print(list2)



list1 = [1,1]
m =1
n = int(input("输入"))
while m<=n:
    num = list1[-1] + list2[-2]
    list1.append(num)
    m +=1

print(list1)



str1 = 'welocme to super&Test'

str2 = str1.split(' ')[-1]
print(str2)
list1 =str2.split('&')
resuil =''.join(list1)
print(resuil)


# str1 = 'welocme to super&Test'
# str2= []
#
# for i in str1.split(" "):
#     i = list(i)
#
#     n =0
#     while n < len(i)/2:
#         i[n],i[len(i)-n-1]=i[len(i)-n-1],i[n]
#         n +=1
#         str2.append(''.join(i))
#     result = ''.join(str2[::-1])
#     print(result)

str1 = 'welocme to super&Test'
str2 = []
for i in str1.split(' '):
    i = list(i)
    #实现单个字符串反转
    n = 0
    while n < len(i)/2:
        i[n],i[len(i)-n-1] = i[len(i)-n-1],i[n]
        n += 1
    # 将反转后字符串拼接，然后追加到新列表中
    str2.append(''.join(i))
    # 倒叙输出并通过空格隔开每次反转后的字符串
result = ' '.join(str2[::-1])
print(result)


str1 = 'abcdef'
str2 = list(str1)
n =0
while n <len(str2)/2:
    tmp = str2[n]
    str2[2]=str2[len(str2)-n-1]
    str2[len(str2)-n-1]=tmp
    n ==1

print(str2,str1)
print("".join(str2))
