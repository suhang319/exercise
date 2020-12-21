#_*_ coding:utf-8 _*_
#@Time      :2020-12-0611:58
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :函数循环调用.py
#@Software:PyCharm



def print_t():
    print("_" * 10)


print_t()

def print_ts(num):
    i =0
    while i < num:
        print_t()

        i+=1

print_ts(10)


