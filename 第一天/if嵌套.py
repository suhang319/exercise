#_*_ coding:utf-8 _*_
#@Time      :2020-11-1516:35
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :if嵌套.py
#@Software:PyCharm

# money = 1
# seat = 0
# if money ==1:
#     print("有钱可以上车")
#     if seat == 1:
#         print("有座可以坐下")
#     else:
#         print("没有座位")
# else:
#     print("没钱上车")


money = int(input("有没有钱："))
seat = int(input("有没有做："))
if money ==1:
    print("有钱可以上车")
    if seat == 1:
        print("有座可以坐下")
    else:
        print("没有座位")
else:
    print("没钱上车")