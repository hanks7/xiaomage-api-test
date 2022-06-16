# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : conftest.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-05-02 14:45
# @Copyright: 北京码同学
from typing import List

import pytest

from requests_study.cookie_study import login


@pytest.fixture(scope='session',autouse=True)
def login_and_logout():
    print('这是conftest.py中定义的fixture')
    login(userName='shamo', password='123456')
    print('在当次执行测试中只执行一次，因为我现在是session作用域')
    yield
    print('在当次执行测试后只执行一次后置动作，因为我现在是session作用域')

# 重写pytest的一个hook函数，处理pycharm插件界面显式的执行结果乱码
def pytest_collection_modifyitems(items:List["Item"]):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")