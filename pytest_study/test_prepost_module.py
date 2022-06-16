# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_prepost_module.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 20:36
# @Copyright: 北京码同学

# 查询余额接口在调用前需要先完成登录接口，否则会报错用户未登录
import pytest

from requests_study.cookie_study import login, query

# @pytest.fixture(scope='module')
# def login_and_logout():
#     print('在当前脚本文件中，测试开始前只执行一次登录')
#     login() #先完成登录接口调用
#     yield
#     print('在当前脚本文件中，所有测试执行之后只执行一次')
# def setup_module():
#     print('在当前脚本文件中，测试开始前只执行一次登录')
#     login() #先完成登录接口调用
# def teardown_module():
#     print('在当前脚本文件中，所有测试执行之后只执行一次')
# 测试用例1：查询余额正确
@pytest.mark.usefixtures('login_and_logout')
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
@pytest.mark.usefixtures('login_and_logout')
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
