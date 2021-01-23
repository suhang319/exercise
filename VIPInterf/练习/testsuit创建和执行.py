#_*_ coding:utf-8 _*_
#@Time      :2021-01-1921:17
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :testsuit创建和执行.py
#@Software:PyCharm

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
class myTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('所有用例的初始化操作')
    @classmethod
    def tearDownClass(cls) -> None:
        print('所有用例的清理工作')

    def setUp(self) -> None:
        print('一个用力的初始化操作')
    def tearDown(self):
        print('一个用例的清理工作')
    def test_add(self):
        print('执行tesrt_add方法')
        self.assertEqual(add(1,2),3)
    def test_mul(self):
        print('执行test_mul方法')
        self.assertEqual(multi(1,2),2)


if __name__ == '__main__':
    unittest.main()

    # 实例化suit
    suit=unittest.TestSuite()
    # 调用addtest方法
    suit.addTest(myTest('test_add'))
    print('suit内',suit)

#     实例化testrunner
    runner=unittest.TestRunner
    runner.run(suit)



