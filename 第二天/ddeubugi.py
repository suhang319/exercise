#_*_ coding:utf-8 _*_
#@Time      :2020-12-0219:40
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :ddeubugi.py
#@Software:PyCharm


"""
方法二： 使用count()函数。如果数量大于1， 并且count()是几，就删除几次

"""


list_t0 = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7, 3]
list_t = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7, 3]
for i in range(0, len(list_t0) + 1):
    print(list_t0.count(i))
    if list_t0.count(list_t0[i]) > 1:
        list_t.remove(list_t0[i])

print(list_t)