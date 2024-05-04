#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/8/29 22:15
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re

import execjs
import requests

url='https://www.cnpcbidding.com/cms/css/bj.css'
#
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'}
resp=requests.get(url,headers=headers).text
res=re.findall('url\(data:image/png;base64,(.*?)\)',resp,re.S)
logo1=res[0]
data=execjs.compile(open('r.js','r',encoding='utf-8').read()).call('jiami',logo1)
print(data)
logo2=res[1]
# print(logo1,)
# print(logo2)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'MACHINE_CODE': '1692184389130',
    'Origin': 'https://www.cnpcbidding.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnpcbidding.com/?',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# json_data = 'J6LQlS+JKK2fwQoSZafwXXejpwzryihZwzB93N2xVYpeEj9EEuDb90R9LcOLynPQvU9QABy31ZuvNPWP+/a6x66ynLIMb8rGzfuBzPJ0zHvd7xotxgnIWFzpP9+WwIE0nymV4Ya5iS6vMRwrRN4HE/LnBgTpeU/dmfIAZovhrMJDJklEmyd34XVyJovKqmYAoiLP7AToSagdd66jMstP2mkrNY2gJnM+99F1dYYpYBDrJLenRiEU8+gPZjKaxiFNLRsYV8kAiKH1wWxLN+D/pO7dY60dhzyOM19+Mu7yAMSq0o+iI6ZZqEz1rOcXpsM+VBCUEgCDCpaISZ32bS7oBg=='
#
# response = requests.post('https://www.cnpcbidding.com/cms/article/page', ALL_headers=ALL_headers, json=json_data).json()
# print(response)