#coding:utf-8_
#@Time      :2020-12-0617:59
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :文件操作.py
#@Software:PyCharm


f = open('testc.txt','w')
f.write("hello\n" 'fjdsjf\n' )
# print(f)
a=  f.readlines()
print(f"{a}")
f.close()
# 读取所有行
content = f.readlines()
print(content)
f.close()

# 一次读取一行内容


f =open('test.txt')

content= f.readable()
print(f"第一行:{content}")

content=f.readable()
f.close()


# seek()
# 文件对象.seek(偏移量，起始位置)
