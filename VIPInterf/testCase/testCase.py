#_*_ coding:utf-8 _*_
#@Time      :2021-01-1320:55
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :testCase.py
#@Software:PyCharm

'''
功能描述：
编写人：
编写日期：

步骤分析：
    1-导入 common.readExcel模块，调用add方法，获取测试数据
    2-根据获取的测试数据的请求方式进行判断
        2.1get 则调用request,get()
        2.2 post
    3-断言接口
    相等=success
    不等=fail
    4.写入Excel


'''

import ddt
import requests
import unittest
from ddt import ddt,data,unpack
from common.readExcel import ReadExcel
from common.configHttp import ConfigHttp

re=ReadExcel()
datelist=re.getdict()
print(datelist)
@ddt
class TestCase(unittest.TestCase):
    @data(*datelist)
    @unpack

    def testrun(self,id,interfaceUrl,name,Method,value,expect,real,status):
        print('----',id,interfaceUrl,name,Method,value,expect,real,status)

        ch =ConfigHttp(interfaceUrl,value,Method,expect)
        realError=ch.run()
        status='Fail'
        self.assertEqual(str(expect),str(realError))
        status='Success'

if __name__ == '__main__':

    unittest.main()