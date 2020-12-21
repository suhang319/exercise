#_*_ coding:utf-8 _*_
#@Time      :2020-12-1318:35
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :异常处理.py
#@Software:PyCharm


try:
    f = open('test.txt',"r")

except:
    f =open('text.txt','w')




#try:
    # 可能发生的异常
# except 异常类型：
#     如果捕获到该异常类型执行的代码


try:
    print(num)

except NameError:
    print("有错误")

try:
    print(1/0)
except (NameError,ZeroDivisionError) as result:
    print(result)

try:
    print(1/0)
except (NameError,ZeroDivisionError) :
    print("有错误")

try:
    print(num)

except Exception as result:
    print(result)


try:
    print(1)
except Exception as result:
    print(result)


else:
    print("没有异常执行代码")

try:
    print(1)
except Exception as result:
    print(result)


else:
    print("没有异常执行代码")

finally:
    f.close()





