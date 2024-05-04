#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/8 15:12
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re

import requests

cookies = {
    'a1': '1897da02d4b455unsq067nfelmvt4l1sc7p3xus1350000112133',
    'webId': '440f0cd1983884c8b68b46141f2c9b5c',
    'gid': 'yYjWf084jJSjyYjWf08JfW7M4D4227IMA8KWUyqIid16hq28941yMC888yyJyqq8id2j4yS2',
    'web_session': '030037a3889a8c3716fbb488c3234a091721b6',
    'abRequestId': '440f0cd1983884c8b68b46141f2c9b5c',
    'xsecappid': 'xhs-pc-web',
    'cacheId': '283f5d7f-b830-4694-ac1f-38274c496186',
    'webBuild': '3.14.1',
    'cache_feeds': '[]',
    'unread': '{%22ub%22:%226520970e000000001e02dcec%22%2C%22ue%22:%2265406d34000000001d015756%22%2C%22uc%22:27}',
    'websectiga': '634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a',
    'sec_poison_id': '11ba215d-37cf-4f31-866c-4265ab66a453',
}

headers = {
    'authority': 'www.xiaohongshu.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'a1=1897da02d4b455unsq067nfelmvt4l1sc7p3xus1350000112133; webId=440f0cd1983884c8b68b46141f2c9b5c; gid=yYjWf084jJSjyYjWf08JfW7M4D4227IMA8KWUyqIid16hq28941yMC888yyJyqq8id2j4yS2; web_session=030037a3889a8c3716fbb488c3234a091721b6; abRequestId=440f0cd1983884c8b68b46141f2c9b5c; xsecappid=xhs-pc-web; cacheId=283f5d7f-b830-4694-ac1f-38274c496186; webBuild=3.14.1; cache_feeds=[]; unread={%22ub%22:%226520970e000000001e02dcec%22%2C%22ue%22:%2265406d34000000001d015756%22%2C%22uc%22:27}; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=11ba215d-37cf-4f31-866c-4265ab66a453',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

response = requests.get('https://www.xiaohongshu.com/user/profile/61adffed0000000010004cd1', cookies=cookies, headers=headers).text
ds=re.findall('window\.__INITIAL_STATE__=(.*)',response)
dsa=str(ds)
print(dsa)
dsd=re.findall('\"nickName\"\:\"(.*?)\"',dsa)[0]
id_s=re.findall('\"redId\"\:\"(.*?)\"',dsa)[0]
count_1=re.findall('\"count\"\:\"(.*?)\"',dsa)[0]
count_2=re.findall('\"count\"\:\"(.*?)\"',dsa)[1]
count_3=re.findall('\"count\"\:\"(.*?)\"',dsa)[2]
print(dsd,id_s,count_1,count_2,count_3)