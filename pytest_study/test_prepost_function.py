# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_prepost_function.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 20:47
# @Copyright: 北京码同学

from requests_study.cookie_study import login, query


def setup_function():
    print('在当前文件中，每个测试用例执行之前都会执行一次')
    login() #先完成登录接口调用
def teardown_function():
    print('在当前脚本文件中，每个测试用例执行之后都会执行一次')
# 测试用例1：查询余额正确
def test_query():
    resp = query(userName='shamo')
    # 做断言
    status_code = resp.status_code
    assert status_code == 200
    print(resp.json())
    # 判断message字段
    message = resp.json()['message']
    assert message == 'success'
    # 判断code值
    code = resp.json()['code']
    assert code == '0'
# 测试用例2：查询余额传入错误用户名，查询失败
def test_query1():
    resp = query(userName='shdhdh')
    # 做断言
    status_code = resp.status_code
    assert status_code == 200
    print(resp.json())
    # 判断message字段
    message = resp.json()['message']
    assert message == '用户未登录'
    # 判断code值
    code = resp.json()['code']
    assert code == '1'