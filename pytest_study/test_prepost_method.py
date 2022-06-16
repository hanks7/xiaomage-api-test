# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_prepost_method.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 20:55
# @Copyright: 北京码同学
import pytest

from requests_study.cookie_study import login, query


class TestQuery:

    def setup_method(self):
        print('在当前类中，每条测试用例执行之前都会执行一次')
        login()
    def teardown_method(self):
        print('在当前类中，每条测试用例执行完成之后都会执行一次')


    # 测试用例1：查询余额正确
    def test_query(self):
        resp = query(userName='shamo')
        # 做断言
        status_code = resp.status_code
        assert status_code == 200
        print(resp.json())
        # 判断message字段
        message = resp.json()['message']
        # assert message == 'success'
        pytest.assume(message == 'success1',f'实际值:{message},期望值:success')
        # 判断code值
        code = resp.json()['code']
        # assert code == '0'
        pytest.assume(code == '1', f'实际值:{code},期望值:0')

    # 测试用例2：查询余额传入错误用户名，查询失败
    def test_query1(self):
        resp = query(userName='shdhdh')
        # 做断言
        status_code = resp.status_code
        assert status_code == 200
        print(resp.json())
        # 判断message字段
        message = resp.json()['message']
        # assert message == '用户未登录'
        pytest.assume(message == '用户未登录', f'实际值:{message},期望值:用户未登录')
        # 判断code值
        code = resp.json()['code']
        # assert code == '1'
        pytest.assume(code == '1', f'实际值:{code},期望值:1')

# 在这些前置后置中，哪个的作用域最大呢
# 模块级别最大，因为不管是函数式测试用例，还是类方式的测试用例，都是在一个模块中的
# 函数级别仅仅是针对，函数式测试用例生效
# 类级别和方法级别，是针对类方式编写测试用例生效
# setup和teardown是可以替换函数级别和方法级别的前置后置
