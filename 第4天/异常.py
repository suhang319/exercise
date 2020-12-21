#_*_ coding:utf-8 _*_
#@Time      :2020-12-1822:44
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :异常.py
#@Software:PyCharm


try:
    f =open("text.txt",'r')

except:
    f =open('text.txt','w')


'''''
try:
    可能发生错误的代码
    
except 异常类型:
    如果捕获到该异常类型执行的代码

'''

try:
    print(num)

except NameError:
    print("有错误")