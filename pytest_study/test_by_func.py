# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_by_func.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 20:01
# @Copyright: 北京码同学

# 以函数形式编写测试用例


from requests_study.cookie_study import login

# 测试用例1：登录用户名密码正确
def test_login():
    # 调用目标接口，传入测试数据,resp是响应对象
    resp = login(userName='shamo',password='123456')
    # 针对接口响应结果做判断
    # 针对结果做判断的这个过程，我们把他叫做断言
    # 对于接口来说，我们关注的是响应状态码，以及响应body信息中的核心字段
    status_code = resp.status_code
    assert status_code == 200 # 断言
    # 针对响应body体信息中的code字段做判断，code为0说明业务成功
    resp_json = resp.json()
    print(resp_json)
    code = resp_json['code'] # 提取code值
    assert code == '0'
    message = resp_json['message']
    assert message == 'success'

# 测试用例2：用户名为空，密码正确
def test_login_userisnull():
    # 调用目标接口，传入测试数据,resp是响应对象
    resp = login(userName='',password='123456')
    # 对于接口来说，我们关注的是响应状态码，以及响应body信息中的核心字段
    status_code = resp.status_code
    assert status_code == 200 # 断言
    # 针对响应body体信息中的code字段做判断，code为0说明业务成功
    resp_json = resp.json()
    print(resp_json)
    code = resp_json['code'] # 提取code值
    assert code == '1'
    message = resp_json['message']
    assert message == '参数为空'