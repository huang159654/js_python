#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/9/21 19:23
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests

cookies = {
    'ZHID': 'EFC092FC8ACBB72B9F311E9EC5BEF759',
    'zh_visitTime': '1695129402696',
    'zhffr': 'read.zongheng.com',
    'PassportCaptchaId': '7bdcf0da2ebcc13f96da7d1eca68c9a2',
    'Hm_lvt_c202865d524849216eea846069349eb9': '1695129403',
    '__zhs__': 'c645f4d28d12fcfcd61db5cdf87feb8742a3259d68eee2c9fda1d6d049197fe1c8f1545edeb6b3ef266676e0981e14a7c118762441eb23a6d545517701b4f709a79016f5617c3fb0b238e7074a22f77544d047f76b27c63750d421c5d2c539d2356aadb90c11b8f71c3004fa28c6b49dcc544c5c32a7ec082c3aeb0361fae61d93f958e621565a81867edd1bbb9648e2eac340af282076b7caf628362c2944d76e5e7a31777b28637c3f22721b8b812b9fc3388911a7b95a240d2ec4a0da8851dc0d48d76030de6b033b39cd00ebec29da199da8acde8f7493946f955ec8e5a789e6f035b5738ddeb3a4593bed002051e2ea95ceb3346424ba089da3e2f071a3',
    '__zhc__': '30820122300d06092a864886f70d01010105000382010f003082010a0282010100eef7bc5b970e91a428e65907609f56f77a6d1ee26ee4fd9f67040fc5e5bbf0b417bc95d2dd309cd4411da92574a6665a3275756cd1626108af9ff62c1d2e18c4fb8bfdb4fe976a82b36d7c41ce78b676b9c8aff41070afecc279c29a248b07413b129b89030ef713f1123b1ace6197901d19414d64fc08b1921aaa928aa5b5f09e4d56e928a613b5354f51921429c1cc108695f3ffd932eff89a7355f2c12f8669c1f486290c47a845b2839ac12d7bbba062a183ec5d8311039443bd18d83efd1d5114ce6ed9ba58e99e9c38e8b4e634c2a2c6374a2c632705e865bb9d4963610280b9c03a209fb92e4d3796b48cca73307c2a1da13812d8a23d9abc234828b70203010001',
    'loginphone': '18259534453',
    '__zhct': '7c464044942548de06b9e2933590bb23.1695134829094',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218aad95fe0b897-0268dcc1d7de1e-26031f51-921600-18aad95fe0c922%22%2C%22%24device_id%22%3A%2218aad95fe0b897-0268dcc1d7de1e-26031f51-921600-18aad95fe0c922%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'Hm_lpvt_c202865d524849216eea846069349eb9': '1695296136',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'ZHID=EFC092FC8ACBB72B9F311E9EC5BEF759; zh_visitTime=1695129402696; zhffr=read.zongheng.com; PassportCaptchaId=7bdcf0da2ebcc13f96da7d1eca68c9a2; Hm_lvt_c202865d524849216eea846069349eb9=1695129403; __zhs__=c645f4d28d12fcfcd61db5cdf87feb8742a3259d68eee2c9fda1d6d049197fe1c8f1545edeb6b3ef266676e0981e14a7c118762441eb23a6d545517701b4f709a79016f5617c3fb0b238e7074a22f77544d047f76b27c63750d421c5d2c539d2356aadb90c11b8f71c3004fa28c6b49dcc544c5c32a7ec082c3aeb0361fae61d93f958e621565a81867edd1bbb9648e2eac340af282076b7caf628362c2944d76e5e7a31777b28637c3f22721b8b812b9fc3388911a7b95a240d2ec4a0da8851dc0d48d76030de6b033b39cd00ebec29da199da8acde8f7493946f955ec8e5a789e6f035b5738ddeb3a4593bed002051e2ea95ceb3346424ba089da3e2f071a3; __zhc__=30820122300d06092a864886f70d01010105000382010f003082010a0282010100eef7bc5b970e91a428e65907609f56f77a6d1ee26ee4fd9f67040fc5e5bbf0b417bc95d2dd309cd4411da92574a6665a3275756cd1626108af9ff62c1d2e18c4fb8bfdb4fe976a82b36d7c41ce78b676b9c8aff41070afecc279c29a248b07413b129b89030ef713f1123b1ace6197901d19414d64fc08b1921aaa928aa5b5f09e4d56e928a613b5354f51921429c1cc108695f3ffd932eff89a7355f2c12f8669c1f486290c47a845b2839ac12d7bbba062a183ec5d8311039443bd18d83efd1d5114ce6ed9ba58e99e9c38e8b4e634c2a2c6374a2c632705e865bb9d4963610280b9c03a209fb92e4d3796b48cca73307c2a1da13812d8a23d9abc234828b70203010001; loginphone=18259534453; __zhct=7c464044942548de06b9e2933590bb23.1695134829094; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218aad95fe0b897-0268dcc1d7de1e-26031f51-921600-18aad95fe0c922%22%2C%22%24device_id%22%3A%2218aad95fe0b897-0268dcc1d7de1e-26031f51-921600-18aad95fe0c922%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_c202865d524849216eea846069349eb9=1695296136',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = ''
response = requests.get(
    'https://read.zongheng.com/chapter/1258940/71173044.html',
    params=params,
    cookies=cookies,
    headers=headers,
).text
print(response)