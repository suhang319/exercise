#_*_ coding:utf-8 _*_
#@Time      :2020-11-1622:47
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :数据格式转换.py
#@Software:PyCharm

# # 输入一个数
# sum = input("请输入一个数：")
# # 打印这个数
# print(f"您输入的数据是{sum}")
# # 打印这个数据格式
# print(type(sum))
# # 将字符串转换为整型
# print(type(int(sum)))
#
#
# # 转换为浮点型
# num1 = 1
# print(float(num1))
# print(type(float(num1)))
# # 转换为字符串类型
# num2=2
# print(type(str(num2)))

# 将一个序列转换为元组
# num3 = [10,20.30]
# print(tuple(num3))
# print(type(num3))
# print(type(tuple(num3)))

# 将一个序列转换为一个列表
# t1 = (10,20,30)
# print(type(t1))
# print(list(t1))
# print(type(list(t1)))


# 将字符串中数据转换为原本样式
str1 = '10'
str2 = "(10,20,30)"
str3 = "[100,200,300]"
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))