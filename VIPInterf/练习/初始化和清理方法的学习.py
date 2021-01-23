# _*_ coding:utf-8 _*_
# @Time      :2021-01-1423:40
# @Author    :lemon_suhang
# @Email  :1147967632@qq.com
# @File   :初始化和清理方法的学习.py
# @Software:PyCharm

'''
功能描述：
编写人：
编写日期：

步骤分析：
    1-
    2-
    3-


'''

import unittest
from common.myfun import *


class TestMyFun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('这是所有的测试用例前的准备工作')

    @classmethod
    def tearDownClass(cls):
        print('这是所有测试用例后的清洗工做')

    def setUp(self):
        print('这是一个测试用例得的准备工作')

    def tearDown(self):
        print('这是一个测试用例结束后的清理工作')

    def test_add(self):
        print('这是TEST开头的方法')


        self.assertEqual(3, add(1, 2))
        self.assertEqual(1, 2, '1!=2')
        self.assertNotEqual(3, add(2, 2))
if __name__ == '__main__':
    unittest.main(verbosity=2)
