#_*_ coding:utf-8 _*_
#@Time      :2020-11-2115:19
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :火车站安检.py
#@Software:PyCharm


# has_ticket= True
#
# knife_ticket=30
#
# if has_ticket:
#     print("车票通过，可以上车")
#
#     if knife_ticket>20:
#         print("刀的长度过长，有%d长" % knife_ticket)
#
#     else:
#         print("安检通过，祝您旅途愉快")
#
# else:
#     print("请先买票")





for i in range(5):
    for j in range(0, 5 - i):
        print(end=" ")
    for k in range(5- i, 5):
        print("*", end=" ")

    print("")


