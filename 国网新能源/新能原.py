#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/8/1 1:30
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests
import execjs
x='{"page":1,"pageSize":50,"gcNo":"","gcName":"","provinceNo":"","prjName":"","energyType":"","installedCapBegin":"","installedCapEnd":"","runDateStart":"","runDateEnd":"","priceType":"","targetPriceBegin":"","targetPriceEnd":"","releaseBatch":"30084003","releaseTimeBegin":"","releaseTimeEnd":"","workType":"","uuid":"f95ced02-2fec-4dd0-b1ef-1e5925a058f5","timestamp":"1690820550466"}'

data=execjs.compile(open('x_dome.js','r',encoding='utf-8').read()).call('jiami',x)
# print(data)
cookies = {
    'PW9ydXnjjO8XS': '5sGJn6kwqjnGYqI4lv4b0wRS0nmQgxc0XUXtsgLt5uybwL_5AotJn5CxVMSMl3iiwfTYf6kAeVxLGj0GKooekTA',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22189cb99f949132f-08a9e398c151ea-26031c51-921600-189cb99f94a1131%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22189cb99f949132f-08a9e398c151ea-26031c51-921600-189cb99f94a1131%22%7D',
    'SERVERID': 'd9f8262d9fcf0d4644e8ea4fbe09573e|1691338022|1691338018',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'PW9ydXnjjO8XS=5sGJn6kwqjnGYqI4lv4b0wRS0nmQgxc0XUXtsgLt5uybwL_5AotJn5CxVMSMl3iiwfTYf6kAeVxLGj0GKooekTA; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22189cb99f949132f-08a9e398c151ea-26031c51-921600-189cb99f94a1131%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22189cb99f949132f-08a9e398c151ea-26031c51-921600-189cb99f94a1131%22%7D; SERVERID=d9f8262d9fcf0d4644e8ea4fbe09573e|1691338022|1691338018',
    'Origin': 'https://sgnec.sgcc.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://sgnec.sgcc.com.cn/atlas/projectListQuery?id=2&releaseBatch=30084003',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sign': '2d73d56bbd57ba644bf7333db8fbf3b7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timestamp': '1691338015966',
}

json_data = data
# print(json_data)

response = requests.post(
    'https://sgnec.sgcc.com.cn/face/tariffsubsidy/centralizedsubsidycontents/listalreadysubsidycontentstable',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
print(response)