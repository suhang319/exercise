#_*_ coding:utf-8 _*_
#@Time      :2020-11-2321:04
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :作业.py
#@Software:PyCharm
# 1、PDF中while循环的最后两个题目（1-三角形*；2-99乘法表）
# 2、求100以内能被3整除的数，并将作为列表输出
list6 =[]
for i in range(1,100):

    if i%3 ==0:

        list6.append(i)
    print(list6)


list = [x for x in range(1,100) if x%3==0]

print(list)

# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
list = [1,2,3,4,3,4,2,5,5,8,9,7]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)


 # 4、求斐波那契数列 1 1 2 3 5 8 13 ……

# 1 1 2 3 5 8 13
a,b = 0, 1
while b<100:
     print (b)
     a, b = b, a+b


# 5、求100以内的质数（只能被1和它本身整除）

sum=[]
a =2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        sum.append(i)
print(sum)

# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
tstr ='aabbbcddef'
a= tstr[5:10:1]
b = a.split("dd")
print(''.join(b))

# 7、有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引

str1='welocme to super&Test'
q = str1.split("&")
a=''.join(q)

print(a[11::1])

# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……
a ='welocme to super&Test'
print(a[::-1])
# 9、有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，
str1='abcdef'
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end='')

# 10、有一堆字符串，“aabbbcddef”，输出abcdef
str5='aabbbcddef'
a =[]
for i in range(len(str5)):
    if str5[i] not in a:
        a.append(str5[i])

print(type(str(a)))