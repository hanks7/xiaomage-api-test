# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_prepost_class.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 20:52
# @Copyright: 北京码同学
import pytest

from requests_study.cookie_study import login, query


@pytest.fixture(scope='class',autouse=True)
def login_and_logout():
    print('在当前类中，所有测试用例执行之前只执行一次')
    login()
    yield
    print('在当前类中，所有测试用例执行完成之后只执行一次')

class TestQuery:

    # def setup_class(self):
    #     print('在当前类中，所有测试用例执行之前只执行一次')
    #     login()
    # def teardown_class(self):
    #     print('在当前类中，所有测试用例执行完成之后只执行一次')

    # 测试用例1：查询余额正确
    def test_query(self):
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
    def test_query1(self):
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
class TestQuery1:

    # def setup_class(self):
    #     print('在当前类中，所有测试用例执行之前只执行一次')
    #     login()
    # def teardown_class(self):
    #     print('在当前类中，所有测试用例执行完成之后只执行一次')

    # 测试用例1：查询余额正确
    def test_query(self):
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
    def test_query1(self):
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
