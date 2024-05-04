import json
import pprint

import execjs
import requests

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1685698503,1685946816',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1685949675',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1685698503,1685946816; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1685949675',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company/detail?id=002105291239451309',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLUnGV4HTHoKbEsbNxuxmdsUhpUUKvcMtoMqfGfwdLCb8g==',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}

params = {
    'qy_id': '002105291239451309',
    'projectType': '01',
    'pg': '0',
    'pgsz': '15',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/compPerformanceListSys',
    params=params,
    cookies=cookies,
    headers=headers,
).text
json_data=execjs.compile(open('./data.js','r',encoding='utf-8').read()).call('h',response)
json_sa_4=json.loads(json_data)
pprint.pprint(json_sa_4)
data_list =json_sa_4.get('data').get('list')
for data in data_list:
    data_PRJNAME=data.get('PRJNAME')
    print(data_PRJNAME)