# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_param_cartesian.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-24 22:43
# @Copyright: 北京码同学

# 以笛卡尔积的方式参数化
import pytest

from requests_study.put_api_study import put

brand_data = ['Huawei','Xiaomi','Oppo'] # 3组
color_data = ['yellow','red','white'] # 3组
memorySize_data = ['64G','128G','256G'] # 3组
cpuCore_data = ['4核','8核','12核','16核'] # 4组
expect_status_code_data = [200] # 1组
expect_code_data = ['0'] # 1组
expect_message_data = ['更新成功'] # 1组
# 通过笛卡尔积组合完成之后，上述数据会产生多少条测试用例数据呢？
# 3*3*3*4*1*1*1=108条
@pytest.mark.parametrize('brand',brand_data)
@pytest.mark.parametrize('color',color_data)
@pytest.mark.parametrize('memorySize',memorySize_data)
@pytest.mark.parametrize('cpuCore',cpuCore_data)
@pytest.mark.parametrize('expect_status_code',expect_status_code_data)
@pytest.mark.parametrize('expect_code',expect_code_data)
@pytest.mark.parametrize('expect_message',expect_message_data)
def test_put(brand,color,memorySize,cpuCore,expect_status_code,expect_code,expect_message):
    # 调用接口，传递测试数据，拿到响应对象
    resp = put(brand=brand,color=color,memorySize=memorySize,cpuCore=cpuCore)
    # 响应状态码断言
    status_code = resp.status_code
    assert status_code == expect_status_code
    # 针对code值做断言
    code = resp.json()['code']
    assert code == expect_code
    # 针对message做断言
    message = resp.json()['message']
    assert message == expect_message
