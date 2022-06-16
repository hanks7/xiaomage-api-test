# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : cookie_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-13 22:17
# @Copyright: 北京码同学

import requests

# 多个接口使用同一个session对象的话，他会自动的帮我们去管理和关联cookie
session = requests.session()

def login(userName='shamo',password='123456'):
    url = 'http://localhost:9090/bank/api/login'

    # 表单参数
    data = {
        'userName':userName,
        'password':password
    }
    print(f'{url}?userName={userName}&password={password}')
    # 发起接口
    resp = session.post(url=url,data=data)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')
    return resp

def query(userName='shamo'):
    url = 'http://localhost:9090/bank/api/query'

    # 查询参数
    params = {
        'userName':userName
    }
    resp = session.get(url=url,params=params)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')
    return resp

if __name__ == '__main__':
    login()
    query()