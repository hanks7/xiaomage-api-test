# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_fixture_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-05-02 14:16
# @Copyright: 北京码同学
import time

import pytest


@pytest.fixture(scope='session')
def fixture_demo1():
    print('这是第一个fixture')
    yield  time.time()#从这一行开始的下一行是后置动作
    print('这是fixture的后置动作')

def test_a(fixture_demo1):
    print(fixture_demo1)
    print('这是第一条测试用例')

def test_b(fixture_demo1):
    print(fixture_demo1)
    print('这是第二条测试用例')