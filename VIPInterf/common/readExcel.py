# _*_ coding:utf-8 _*_
# @Time      :2021-01-1320:54
# @Author    :lemon_suhang
# @Email  :1147967632@qq.com
# @File   :readExcel.py
# @Software:PyCharm
'''
功能描述：
编写人：
编写日期：

步骤分析：
    1-导入 xlrd包
    2-打开Excel(Excel路径+名称)
    3-确定sheet页
    4.确定所有数据最大行为循环次数
        定义一个数据空列表
        4.1读取每行数据
        4.2从第2行开始读
        4.3读取一行数据后，追加到列表
    5.return返回


'''


import xlrd
import os

class ReadExcel():
    def __init__(self):
        self.value = os.path.dirname(os.path.dirname(__file__))
        self.excel=self.value + r"\testDate\data.xls"
        self.readbook= xlrd.open_workbook(self.excel)
        self.sheet = self.readbook.sheet_by_index(0)

        self.nrows = self.sheet.nrows
        print(self.nrows)
    def read(self):
        dlist=[]
        for i in range(1,self.nrows):
            value=self.sheet.row_values(i)


            dlist.append(value)
            return dlist

    def getdict(self):
        '''
        将获取的数据封装成字典的样子
        :return:
        '''
#         定义一个保存数据的空列表
        datelist=[]
#         获取第1行的值
        keylist=self.sheet.row_values(0)
        for i in range(1,self.nrows):
            valuelist=self.sheet.row_values(i)
            dict ={keylist[j]:valuelist[j] for j in range(len(valuelist))}
            datelist.append(dict)
        return datelist

if __name__ == '__main__':

    re =ReadExcel()
    print(re.read())
    print(re.getdict())
