# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : file_api_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-13 22:50
# @Copyright: 北京码同学
import requests

session = requests.session()
def upload_file():
    url = 'http://localhost:9090/file/api/upload2'

    # 文件参数
    files = {
        'file':open(r'C:\Users\lixio\Desktop\logo.png',mode='rb')
    }
    # 发起接口调用
    resp = session.post(url=url,files=files)
    # 获取响应状态码
    print(f'响应状态码是:{resp.status_code}')
    # 获取响应体信息
    print(f'响应body体信息:{resp.json()}')
if __name__ == '__main__':
    upload_file()
