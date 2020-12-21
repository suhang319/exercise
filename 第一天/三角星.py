#_*_ coding:utf-8 _*_
#@Time      :2020-11-3020:35
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :三角星.py
#@Software:PyCharm

# 长方形
# for i in range(0,5):
#     print("*"*5)


# 左对齐直角三角星
for i in range(5):
    print("*"*i)


     # 左对齐倒着三角形
for i in range(5):
    print((5-i)*"*")

# 右对齐直角三角星

for i in range(5):
    print((5-i)*' '+ i*"*")

# 右对齐倒三角形
for i in range(5):
    print(i*" " + (5-i)*'*')
# 正三角形
for i in range(1,9,2):
    print((9-i)//2*' ' +i*'*')



# 倒三角形
for i in range(1,9,2):
    print(i//2*' ' + (9-i-1)*"*")


    # 菱形
    for i in range(1, 9, 2):
        print((9 - i) // 2 * ' ' + i * '*')
    for i in range(1, 9, 2):
        print((i // 2+2)*' ' + (7 - i - 1) * "*")