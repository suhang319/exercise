#_*_ coding:utf-8 _*_
#@Time      :2020-11-1720:48
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :if嵌套.py
#@Software:PyCharm

# money = int(input("请输入你的钱："))
#
# if money>0:
#     print("有钱可以上车")
#
# else:
#     print("没钱不可以上车")

# money = 1
# seat = 0
# if money ==1:
#     print("有钱可以上车")
#     if seat==1:
#         print("有座位")
#     else:
#         print("站着")
# else:
#     print("地走")



money =int(input("请输入您的钱数："))

if money>0:
    print("有钱可以上车")
    seat = int(input("请输入座位："))
    if seat>0:
        print("可以坐着了")
    else:
        print("没坐了")
else:
    print("没有上去车")