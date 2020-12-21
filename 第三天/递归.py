#_*_ coding:utf-8 _*_
#@Time      :2020-12-0616:02
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :递归.py
#@Software:PyCharm


def sum_numbers(num):
    if num ==1:

        return 1

    return num + sum_numbers(num-1)

sum_result = sum_numbers(3)
print(sum_result)


