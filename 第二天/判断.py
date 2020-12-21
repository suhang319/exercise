#_*_ coding:utf-8 _*_
#@Time      :2020-11-2213:54
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :判断.py
#@Software:PyCharm


mystr = "hello world and supertest and chaoge  and python"
# startswith用法
# print(mystr.startswith("hello"))
#
# print(mystr.startswith('hello',5,20))


# endswith用法
# print(mystr.endswith("python"))
# print(mystr.endswith("pytho"))
# print(mystr.endswith("python",2,20))

# isalpha()
# mystr1 = 'hello'
# mystr2 ='hello12345'
# print(mystr1.isalpha())
# print(mystr2.isalpha())

# isdigit(）用法
# mystr1 = 'hello12345'
# mystr2 ='2345'
# print(mystr1.isdigit())
# print(mystr2.isdigit())


# isalnum(）用法
# mystr1 = 'hello12345'
# mystr2 ='2345@@@@'
# print(mystr1.isalnum())
# print(mystr2.isalnum())
#
# # isspace()用法
# mystr1 = '1 2 3 4 5'
# mystr2 ='      '
# print(mystr1.isspace())
# print(mystr2.isspace())


range(4,-1,-1)
print(range)

a,b = 0, 1
while b<100:
     print (b)
     a, b = b, a+b