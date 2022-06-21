# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_param_login.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 22:29
# @Copyright: 北京码同学

# 使用参数化方式实现登录接口的测试

# 第一步，将测试数据转换为python中列表套列表的形式
import pytest

from datadriver_study.file_operate import read_excel, read_yaml
from requests_study.cookie_study import login

# test_data = [
#     ['shamo','123456',200,'0','success'],
#     ['',     '123456',200,'1','参数为空'],
#     ['shamo','',      200,'1','参数为空']
# ]
# test_data = read_excel(r'D:\pycharmprojects\testpro1\datadriver_study\test_data.xlsx','登录接口数据')
#正确的
# test_data = read_yaml(r'E:\DocumentWork\projectPython\github-xiaomage-api-test\datadriver_study\test_data.yml')['登录接口数据']
#正确的
# test_data = read_yaml(r'..\datadriver_study\test_data.yml')['登录接口数据']
test_data = read_yaml(r'../datadriver_study/test_data.yml')['登录接口数据']
# 第二步，使用pytest装饰器，读取上述数据，将其传递给测试用例函数
@pytest.mark.parametrize('userName,password,expect_status_code,expect_code,expect_message',test_data)
def test_login(userName,password,expect_status_code,expect_code,expect_message):
    # 调用接口，传递测试数据，得到响应对象
    resp = login(userName=userName,password=password)
    # 针对响应状态码做断言
    status_code = resp.status_code
    assert status_code == expect_status_code
    # 针对code值做断言
    code = resp.json()['code']
    assert int(code) == expect_code
    # 针对message做断言
    message = resp.json()['message']
    assert message == expect_message