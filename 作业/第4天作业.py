#_*_ coding:utf-8 _*_
#@Time      :2020-12-1920:29
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :第4天作业.py
#@Software:PyCharm
# 1.列表[1,2,3,4,5,5,2,3,2,4]	去重，不能使用现有函数
# 定义一个空列表，循环这个列表，如果这些数不在空列表内，则添加进入
list =[1,2,3,4,5,5,2,3,2,4]
list1=[]

for i in list:
    if i not in list1 :
        list1.append(i)
print(list1)

# 4.文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
# lucy:21，tom:30
# xiaoming:18，xiaohong:15
# xiaowang:20，xiaohei:19
# 输出年龄大于18岁的人名

'''''
1.读取文件用readlines  读出是个列表
2.定义一个列表 ，循环文件内容
3.去除换行和,
4.循环这个列表去除：
5.定义一个空字典，用字典接受
6.循环这个字典
7.大于18的，打印出

'''
f = open("./date.txt",'r',endcoding='utf=-8')
content=f.readlines()
list01=[]
dict1={}
for i in content:
    a=i.split('\n')
    list01=a.split(',')
    print(list01)
    for j in list01:
         list02=j.split(":")
         print(list02)
         dict1[list02[0]]=int(list02[1])

for key,value in dict1.items():
    if value>18:
        print(f"{key}大于18岁")



# 7.有一堆字符串，“welocme to super&Test”，
# 打印出emcolew ot  tseT&repus……全部单词原位置反转
str1='welocme to super&Test'
list01=[]
list02=str1.split()
for i in list02:
    str2=i.split()
    list01.append(str2)
print(' '.join(list01))


# 10.递归实现斐波那契数列
def fib(n):
    if n <=1:
        return n

    else:
        return fib(n-1) + fib(n-2)

n =int(input("请输入你需要的序列个数："))
for i in range(n):
   a= fib(i)
   print(a)

# 12如何实现[‘1’,’2’,’3’]变成[1,2,3]

list04=['1','2','3']
list05=[]

for i in list04:
    i =int(i)
    list05.append(i)
print(list05)

list7=['1','2','3']
list8=[int(i) for i in list7]
print(list8)

# 13、开发一个注册系统，保存用户名和密码，存在的用户提示已注册，不存在的可以注册成功


list9=[]
def zhuce():
    global list9
    print('-'*20)
    print("----注册用户------")
    user=input("请输入用户名：")
    password=input("请输入密码")
    if len(list9)==0:
        add_user(user,password)
    else:
        panduan(user,password)
    return 0

def add_user(user,password):
    global list9
    dict101={}
    dict101['name']=user
    dict101['password']=password
    list9.append(dict101)
    return 0

def panduan(user,password):
    global list9
    for i in list9:
        if i ["name"]==user:
            print("该用户已存在")
            break




