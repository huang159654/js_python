import json
import pprint

import execjs
import requests

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1685698503,1685946816',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1685946824',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1685698503; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1685702670',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company/detail?id=002105291239451309',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLU2A/VkpttHwfF2K04DcntLhpUUKvcMtoMqfGfwdLCb8g==',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}
params = {
    'compId': '002105291239451309',
}
response = requests.get('https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/compDetail', params=params,cookies=cookies, headers=headers).text
print(response)
# json_data=execjs.compile(open('./data.js','r',encoding='utf-8').read()).call('h',response)
# json_sa=json.loads(json_data)
# pprint.pprint(json_sa)
# json_QY_NAME=json_sa.get('data').get('compMap').get('QY_NAME')#公司名称
# json_QY_ORG_CODE=json_sa.get('data').get('compMap').get('QY_ORG_CODE')#统一社会信用代码
# json_QY_GSZCLX_NAME=json_sa.get('data').get('compMap').get('QY_GSZCLX_NAME')#企业登记注册类型
# json_QY_REGION_NAME=json_sa.get('data').get('compMap').get('QY_REGION_NAME')#企业注册属地
# json_QY_FR_NAME=json_sa.get('data').get('compMap').get('QY_FR_NAME')#法定代表人
# json_QY_ADDR=json_sa.get('data').get('compMap').get('QY_ADDR')#企业经营地址
#
# print(json_QY_NAME,
# json_QY_ORG_CODE,
# json_QY_GSZCLX_NAME,
# json_QY_REGION_NAME,
# json_QY_FR_NAME,
# json_QY_ADDR)