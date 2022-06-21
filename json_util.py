# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : json_util.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-05-04 12:02
# @Copyright: 北京码同学
from jsonpath_rw import Index, Fields
from jsonpath_rw_ext import parse


def update_value_to_json(json_object,json_path,new_value):
    '''
    修改json中某个字段的内容
    比如:
    把userName替换成空字符串
    update_value_to_json(json, '$.userName', '')

    :param json_object:
    :param json_path:
    :param new_value:
    :return:
    '''
    json_path_expr = parse(json_path)

    for match in json_path_expr.find(json_object):
        path = match.path # 这是获取到匹配结果的路径
        if isinstance(path,Index):
            match.context.value[match.path.index] = new_value
        elif isinstance(path,Fields):
            match.context.value[match.path.fields[0]] = new_value
    return json_object

if __name__ == '__main__':
    json = {
        "userName": "test",
        "password": "1234",
        "gender": 1,
        "phoneNum": "110",
        "email": "beihe@163.com",
        "address": "Beijing"
    }
    # 把userName替换成空字符串
    print(update_value_to_json(json, '$.userName', ''))
