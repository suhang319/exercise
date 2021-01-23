#_*_ coding:utf-8 _*_
#@Time      :2021-01-2020:34
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :ddt1.py
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



from ddt import ddt,data,unpack

import unittest
list2=[3,4,5]
test_data=[[1,2],[3,4]]
test_dict=[{'key':1,'key1':2},{'key':1,'key1':3}]
@ddt
class  Mytest(unittest.TestCase):

    @data(1)
    def test_bb1(self,value):
        print(value)
        self.assertEqual(value,2)
    @data(2,3,4)
    def test_bb2(self,value):
        print(value)
        self.assertEqual(value,2)

    @data((1,2))
    @unpack
    def test_bb4(self,value,value1):
        print('--',value,value1)
        self.assertEqual(value,value1)
    @data([1,2],[3,4])
    @unpack
    def test_bb5(self,value3,value4):
        print('--',value3,value4)
        self.assertEqual(value3,value4)
    @data(*test_data)
    @unpack
    def test_abb6(self,value1,value2):
        print('--',value1,value2)
        self.assertEqual(value1,value2)
    @data({'value1':1,'value2':2})
    @unpack
    def test_bb7(self,value1,value2):
        print('--',value1,value2)
        self.assertEqual(value1,value2)

    @data(*test_dict)
    @unpack
    def test_bb8(self,key,key1):
        print('--',key,key1)
        self.assertEqual(key,key1)

if __name__ == '__main__':

    unittest.main(verbosity=2)
