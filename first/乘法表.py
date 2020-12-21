#_*_ coding:utf-8 _*_
#@Time      :2020-11-1920:29
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :乘法表.py
#@Software:PyCharm


i=1

while i<= 9:
    a=1
    while a<=i:
        print(f"{i}*{a}={i*a}",end="/t")
        a+=1

    print()
    i+=1