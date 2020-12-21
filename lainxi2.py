#_*_ coding:utf-8 _*_
#@Time      :2020-12-1311:41
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :lainxi2.py
#@Software:PyCharm

# n 以内的累计和

# 分析  n + n-1 + 1的累加

def sum_a(num):
    if num ==1:
        return 1


    return num + sum_a(num -1)
n=int(input("请输入n"))
sum_result= sum_a(n)

print(sum_result)



# 、求斐波那契数列 1 1 2 3 5 8 13 ……


def sum_b(a):
     if a==1:
         return 1

     for a in range(0,20):
         return a