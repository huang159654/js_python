import json
import pprint

import execjs
import requests

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
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1685698503,1685946816; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1685946824',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company/detail?id=002105291239451309',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLV7PtBtr0zfH+grOdWVakq1hpUUKvcMtoMqfGfwdLCb8g==',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}

params = {
    'qyId': '002105291239451309',
    'pg': '0',
    'pgsz': '15',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/caDetailList',
    params=params,
    cookies=cookies,
    headers=headers,
).text
json_data=execjs.compile(open('./data.js','r',encoding='utf-8').read()).call('h',response)
json_sa_1=json.loads(json_data)
pprint.pprint(json_sa_1)
list_data=json_sa_1.get('data').get('pageList').get('list')
list_data_1=[]
for i in list_data:
    i_APT_NAME=i.get('APT_NAME')
    list_data_1.append(i_APT_NAME)
print(list_data_1)
