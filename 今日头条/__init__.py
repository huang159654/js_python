#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/27 21:50
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests



headers = {
    'authority': 'www.toutiao.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'passport_csrf_token=59492906ca197c1ba73697aeb0b4a7bf; passport_csrf_token_default=59492906ca197c1ba73697aeb0b4a7bf; tt_webid=7340277555364972083; local_city_cache=%E6%80%80%E5%8C%96; s_v_web_id=verify_lt4f729x_2xgMdP2p_q9Ty_4wAK_B5PF_5Bs0DYznaAcA; csrftoken=7e90d11d1b458f4a36395361cba1197e; _ga=GA1.1.908496126.1709041522; _S_DPR=1; _S_IPAD=0; _S_WIN_WH=1920_356; ttwid=1%7CKGNKpTkEs7I83h3_dsacAJf6VEYJqLXiCUJkQjm9At0%7C1709041783%7Cd89220ba49e063be316156e713288481d118e55b9726d2316983515fad22d957; tt_scid=ejSZZ3V2nNRAFyV7Pzy05TjQ3fCZlD.EYZS4jKh65kaQJyer6Z2fPYE4FZh0tyNDce5c; _ga_QEHZPBE5HH=GS1.1.1709041522.1.1.1709041722.0.0.0; msToken=5tRd2BcJiEDO9CYtC6AkFAS32S6fl41X0zh9WmIaPP_hNyajr-E09Z_5OpFVRxcCMI8cGKhK_O6ZES1q70Be3rdJYTX2VYoQWlAJIiDC',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/article/7334544302301151783/?log_from=609a3e78d333f_1709041720894',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}
for offset in range(0,100,20):
    params = {
        'aid': '24',
        'app_name': 'toutiao_web',
        'offset': offset,
        'count': '20',
        'group_id': '7334544302301151783',
        'item_id': '7334544302301151783',
       # '_signature': '_02B4Z6wo00901fo2OZQAAIDCx58jCYUdWqH6Ej0AABtSYAmeDz8Revc4pN-m8pdgxi-RpSYSbQeqojuIPn-3eASwZ8ZCBJK1LWyzJ0v16aVbDNLZe3uGY6NKMKdAxChxirru2vtXGlHvUGbI57',
    }

    response = requests.get('https://www.toutiao.com/article/v4/tab_comments/', params=params,  headers=headers).json()
    list=response['data']
    for d in list:
        print(d['comment']['text'])