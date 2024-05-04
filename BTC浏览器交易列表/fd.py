#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/6 14:18
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import base64

import execjs
import requests
#分析到有两处好像有加密 https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?t=1680689936560&offset=0&txType=&limit=20&sort= 数据地址
#1.在cookie里面'aliyungf_tc': '6f5a570fa0e64f4d30f5600c7d9e112d1851844029dcaf09bfbd9fce60670bc1',
#2.在headers里面 'x-apikey': 'LWIzMWUtNDU0Ny05Mjk5LWI2ZDA3Yjc2MzFhYmEyYzkwM2NjfDI3OTE3ODk5NDczOTg5OTQ=',
# x_apikey = execjs.compile(open('./demo.js','r',encoding='utf').read()).call('getApiKey')
# print(x_apikey)
getApiKey=execjs.compile(open('x-apikey.js', 'r', encoding='utf-8').read()).call('getApiKey')
# print(getApiKey)
source = getApiKey
base64_da=base64.b64encode(getApiKey.encode())
x_apikey=str(base64_da,'utf-8')
print(x_apikey)
# cookies = {
#     'locale': 'zh_CN',
#     'browserVersionLevel': 'v5.6ad2a8e37c01',
#     'devId': '2363b8ed-3c07-41c1-beb3-d9f7bfdfa837',
#     'okg.currentMedia': 'xl',
#     'first_ref': 'https%3A%2F%2Fwww.oklink.com%2Fcn%2Fbtc%2Ftx-list',
#     'aliyungf_tc': '8cd51725141e4827ce6369b6dc71ba6d519d8212cd3f6d83d3a3daf9e4255723',
#     'traceId': '1030197058110650001',
#     '_monitor_extras': '{"deviceId":"TQ7crg3oK5Wa49VXE0oVEJ","eventId":10,"sequenceNumber":10}',
#     'oklink.unaccept_cookie': '1',
#     'amp_d77757': '_-K5PMdkmdajT8naz-XETx...1ho96gnbc.1ho96gnbf.9.0.9',
#     'ok-ses-id': 'guIR1VyATqlu5VBJwp+SjGao2nnuFIe4mLGiuWkOq4my9wD9IHBZ4IQ/YhlhtwwkgXz42256t/gLS0nVXWNkm4GMmBxil+oIeEkZNP7WVyvQGbbNrmQZJCctE3X0/U7H',
# }
# headers = {
#     'authority': 'www.oklink.com',
#     'accept': 'application/json',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'app-type': 'web',
#     'cache-control': 'no-cache',
#     # 'cookie': 'locale=zh_CN; browserVersionLevel=v5.6ad2a8e37c01; devId=2363b8ed-3c07-41c1-beb3-d9f7bfdfa837; okg.currentMedia=xl; first_ref=https%3A%2F%2Fwww.oklink.com%2Fcn%2Fbtc%2Ftx-list; aliyungf_tc=8cd51725141e4827ce6369b6dc71ba6d519d8212cd3f6d83d3a3daf9e4255723; traceId=1030197058110650001; _monitor_extras={"deviceId":"TQ7crg3oK5Wa49VXE0oVEJ","eventId":10,"sequenceNumber":10}; oklink.unaccept_cookie=1; amp_d77757=_-K5PMdkmdajT8naz-XETx...1ho96gnbc.1ho96gnbf.9.0.9; ok-ses-id=guIR1VyATqlu5VBJwp+SjGao2nnuFIe4mLGiuWkOq4my9wD9IHBZ4IQ/YhlhtwwkgXz42256t/gLS0nVXWNkm4GMmBxil+oIeEkZNP7WVyvQGbbNrmQZJCctE3X0/U7H',
#     'devid': '2363b8ed-3c07-41c1-beb3-d9f7bfdfa837',
#     'pragma': 'no-cache',
#     'referer': 'https://www.oklink.com/cn/btc/tx-list/page/2',
#     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
#    'x-apikey': x_apikey,
#     'x-cdn': 'https://static.oklink.com',
#     'x-locale': 'zh_CN',
#     'x-site-info': '[object Object]',
#     'x-utc': '8',
#     'x-zkdex-env': '0',
# }
#
# params = {
#     't': '1709705868879',
#     'offset': '40',
#     'limit': '20',
# }
#
# response = requests.get(
#     'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# ).json()
# print(response)