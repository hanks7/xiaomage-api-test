# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : put_api_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-13 22:11
# @Copyright: 北京码同学

import requests

def put(brand='Huawei',color='yellow',memorySize='64G',cpuCore='8核'):
    url = 'http://localhost:9090/com/phone'

    json = {
        "brand": brand,
        "color": color,
        "memorySize": memorySize,
        "cpuCore": cpuCore,
        "price": "8848",
        "desc": "全新上市"
    }
    # 调用接口
    resp = requests.put(url=url,json=json)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')
    return resp
if __name__ == '__main__':
    put()
