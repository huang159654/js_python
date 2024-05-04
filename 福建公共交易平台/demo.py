import execjs
import requests
import time
for pageNo in range(1,5):
    json_data = {
        "pageNo": 2,
        "pageSize": 20,
        "total": 3751,
        "AREACODE": "",
        "M_PROJECT_TYPE": "",
        "KIND": "GCJS",
        "GGTYPE": "1",
        "PROTYPE": "",
        "timeType": "6",
        "BeginTime": "2023-01-26 00:00:00",
        "EndTime": "2023-07-26 23:59:59",
        "createTime": [],
        "ts": round(time.time() * 1000),
    }
    portal_sign = execjs.compile(open('./portal_sign.js', 'r', encoding='utf_8').read()).call('d', json_data)
    # print(portal_sign)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ggzyfw.fujian.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'portal-sign': portal_sign,
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers,
                             json=json_data).json()
    data = response['Data']
    # print(data)
    sa = execjs.compile(open('cr.js', 'r', encoding='utf-8').read()).call('b', data)
    print(sa)
