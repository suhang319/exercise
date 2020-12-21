#_*_ coding:utf-8 _*_
#@Time      :2020-11-1518:01
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :1到100偶数累加和.py
#@Software:PyCharm


n= 1
sum = 0

while n<=100:
    if n% 2== 1:
        sum += n

    n +=1
print("sum",sum)