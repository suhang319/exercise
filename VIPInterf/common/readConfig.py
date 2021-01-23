#_*_ coding:utf-8 _*_
#@Time      :2021-01-2223:22
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :readConfig.py
#@Software:PyCharm

'''
功能描述： 给一个secion 得到xxoption
编写人：
编写日期：

步骤分析：
    1-
    2-
    3-


'''
import configparser
import os



class ReadConfig():
    def __init__(self):
        self.conf = configparser.ConfigParser()
#         获取当前文件路径
        file_path = os.path.dirname(os.path.dirname(__file__)) + '//config.ini'
        print(file_path)
        self.conf.read(file_path,encoding='utf-8-sig')


    def get_setion(self,name):
        # 获取某个setion下option
        result=self.conf.items(name)
        print(result)

    def get_options(self,name,items):
        value = self.conf.get(name,items)
        print(value)




if __name__ == '__main__':


    a =ReadConfig()
    E=a.get_setion('redis')
    f=a.get_options('redis','ip')
