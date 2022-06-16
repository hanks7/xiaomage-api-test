# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : post_api_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-13 22:01
# @Copyright: 北京码同学

import requests

from json_util import update_value_to_json


def post_data():
    # 表单参数
    url = 'http://localhost:9090/com/login'
    # 表单参数
    data = {
        'userName':'shamo',
        'password':'123456'
    }
    # 调用，拿到结果对象
    resp = requests.post(url=url,data=data)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')

# json_path指的是你要测试的字段对应的jsonpath表达式
# new_value指的是你要测试的字段的新值
def post_json(json_path,new_value):
    url = 'http://localhost:9090/com/register'
    # json参数
    json = {
        "userName": "test",
        "password": "1234",
        "gender": 1,
        "phoneNum": "110",
        "email": "beihe@163.com",
        "address": "Beijing"
    }
    # 使用更新方法，接收用户传进来的测试数据，更新json参数
    json = update_value_to_json(json,json_path,new_value)
    # 声明json对应的content-type 头信息
    # headers = {
    #     'Content-Type':'application/json'
    # }
    print(f'新json：{json}')
    # 发起调用
    resp = requests.post(url=url,json=json)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')
if __name__ == '__main__':
    # post_data()
    post_json('$.userName','') #用户名为空
    post_json('$.password','') # 密码为空
    post_json('$.gender',8) # 性别为8