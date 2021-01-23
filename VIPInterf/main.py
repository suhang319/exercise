#_*_ coding:utf-8 _*_
#@Time      :2021-01-1320:51
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :main.py
#@Software:PyCharm

'''
功能描述：查找所有测试用例，执行测试用例，生成报告
编写人：suhang
编写日期：2021年1月22

步骤分析：
    1-导入unittest,HTMLTestrunner,
    2-使用Testloader查找测试用例
    3-使用Testrunner执行测试用例
    4.借助HTMLTestrunner生成报告
    5.发送测试报告的邮件

'''''

import unittest
import HTMLTestRunner
import os,time

from HTMLTestRunner import HTMLTestReportCN

# 用例所在目录
case_dir= os.path.dirname(os.path.abspath(__file__)) + "\\testCase"


def creat_suit():
    suite=unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py')
    return suite

if __name__ == '__main__':

  suite=creat_suit()
  # 定义报告名称
  timestr = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
  filename =os.path.dirname(os.path.abspath(__file__)) + '\\report\\report' + timestr + '.html'
  # 打开文件 准备写入
  fp =open(filename,'wb')
  # 使用HTMLTestrunner定义报告内容
  runner =HTMLTestReportCN(stream=fp,title='接口自动化测试报告',description='玩安卓项目',tester='suhang')
# 使用runnner执行suit
  runner.run(suite)
  # 关闭文件
  fp.close()