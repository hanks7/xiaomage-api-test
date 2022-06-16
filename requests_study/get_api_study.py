# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : get_api_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-04-13 21:49
# @Copyright: 北京码同学
import requests

# 对于一个接口来说都有哪些信息
# 接口路径、请求headers、请求参数、响应状态码、响应body体信息
def get():
    url = 'http://localhost:9090/com/getSku' # 接口地址
    # 对于get接口来说，他的请求参数类型基本就是查询参数
    params = {
        'id':1
    }
    # 接口请求信息已经准备好了，进行调用
    # resp是响应对象，包括了很多信息，响应headers，响应状态码，响应body体信息
    resp = requests.get(url=url,params=params)
    status_code = resp.status_code #获取响应状态码
    print(f'响应状态码是:{status_code}')
    # 获取响应body体信息
    text = resp.text # 以字符串的形式得到响应的body体信息，text的类型是str
    print(f'响应信息是字符串形式的:{text}')
    # 以json的格式得到响应body体信息
    json1 = resp.json() # json1 要么是列表，要么字典，只能处理响应信息是json格式字符串的
    print(f'响应信息是json格式的:{json1}')
if __name__ == '__main__':
    get()