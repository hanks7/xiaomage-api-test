# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : token_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-13 22:29
# @Copyright: 北京码同学

import requests
import jsonpath
session = requests.session()

def login(userName='shamo',password='123456'):
    url = 'http://localhost:9090/bank/api/login2'
    # 表单参数
    data = {
        'userName':userName,
        'password':password
    }
    # 发起调用
    resp = session.post(url=url,data=data)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    # {'code': '0', 'message': 'success', 'data': 'c4bc1d9a5f32492f81a635598345496c'}
    # 其中data字段对应的值就是服务器返回的token
    print(f'响应body体信息:{resp.json()}')
    print(type(resp.json())) # <class 'dict'> 这说明该接口的resp.json()返回的数据是字典类型
    # 提取token
    global token
    # token = resp.json()['data']

    # 第一个参数表示要解析的目标对象
    # 第二个参数你要提取的数据对应的jsonpath表达式
    # 注意如果表达式能够匹配到数据，不管是1个还是多个，返回结果都是列表，所以最后我们加了一个[0]
    # 注释如果表达式匹配不到数据，那么他的返回值是False
    print(jsonpath.jsonpath(resp.json(),'$.data'))
    token = jsonpath.jsonpath(resp.json(),'$.data')[0]
    return resp

def query():
    url = 'http://localhost:9090/bank/api/query2'
    # 查询参数
    params = {
        'userName':'shamo'
    }
    headers = {
        'testfan-token':token
    }
    # 发起调用
    resp = session.get(url=url,params=params,headers=headers)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')
if __name__ == '__main__':
    login()
    # query()
