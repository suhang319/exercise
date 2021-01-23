#_*_ coding:utf-8 _*_
#@Time      :2021-01-1921:59
#@Author    :lemon_suhang
#@Email  :1147967632@qq.com
#@File   :configHttp.py
#@Software:PyCharm

'''
功能描述：接收testcase传入的接口请求测试数据，根据具体的请求逻辑完成接口测试，将接口返回的关键结果返回给用例即可
编写人：suhang
编写日期：2021年1月19

步骤分析：
    1-接收testcase传入的测试数据 id,name
    2-提取接口的请求方式
    method 判断
    get--- request.get
    post---request.post
    3-返回接口的执行结果
    1.返回后断言
    2.直接断言


'''

import requests


class ConfigHttp():
    def __init__(self,url,param,method,expect):
        self.url=url
        self.param=eval(param)
        self.method=method
        self.expect=expect
        self.header={}

        # 10秒内必须返回
        self.timeout=10



    def run(self):
        ''''对外提供接口请求方法'''
        if self.method.lower() =='get':
            return self.__get()
        elif self.method.lower()=='post':
            return self.__post()
        elif self.method.lower()=='put':
            return self.__put()
        elif self.method.lower()=='delete':
            return self.__delete()



    def __get(self):

        result =requests.get(url=self.url,params=self.param,headers=self.header,timeout=self.timeout)
        realError=result.json()['errorCode']
        return realError
    def __post(self):
        result = requests.post(url=self.url, data=self.param, headers=self.header, timeout=self.timeout)
        realError = result.json()['errorCode']
        return realError
    def __put(self):
        result = requests.put(url=self.url, data=self.param, headers=self.header, timeout=self.timeout)
        realError = result.json()['errorCode']
        return realError
    def __delete(self):
        result = requests.delete(url=self.url, headers=self.header, timeout=self.timeout)
        realError = result.json()['errorCode']
        return realError


if __name__ == '__main__':
    datelist=[{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'expect': '0', 'real': '', 'status': ''},
              {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'liangchao03','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''},
              {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'Get', 'value': "{'username':'liangchao'}", 'expect': '0', 'real': '', 'status': ''}]


    url=datelist[0]['interfaceUrl']
    param=datelist[0]['value']
    Method=datelist[0]['Method']
    expect=datelist[0]['expect']

    ch =ConfigHttp(url,param,Method,expect)
    re =ch.run()
    print(ch)