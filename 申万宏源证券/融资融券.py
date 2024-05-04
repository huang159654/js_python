import requests
import execjs

cookies = {
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218760cd4303bc3-0418cad55e52bc-26031851-921600-18760cd4304e17%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3NjBjZDQzMDNiYzMtMDQxOGNhZDU1ZTUyYmMtMjYwMzE4NTEtOTIxNjAwLTE4NzYwY2Q0MzA0ZTE3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218760cd4303bc3-0418cad55e52bc-26031851-921600-18760cd4304e17%22%7D',
    'Hm_lvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c': '1683180595,1684597377,1685540520',
    'Hm_lpvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c': '1685690005',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218760cd4303bc3-0418cad55e52bc-26031851-921600-18760cd4304e17%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3NjBjZDQzMDNiYzMtMDQxOGNhZDU1ZTUyYmMtMjYwMzE4NTEtOTIxNjAwLTE4NzYwY2Q0MzA0ZTE3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218760cd4303bc3-0418cad55e52bc-26031851-921600-18760cd4304e17%22%7D; Hm_lvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c=1683180595,1684597377,1685540520; Hm_lpvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c=1685690005',
    'Pragma': 'no-cache',
    'Referer': 'https://www.swhysc.com/swhysc/financial/marginTradingList?channel=00010017000300020001&listId=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'secuCode': '',
    'market': '',
    'orderFlag': '',
    'pageNum': '2',
    'pageSize': '10',
}

response = requests.get(
    'https://www.swhysc.com/swhyscywbl/service/dsinfo/v1/margin/conver/rate',
    params=params,
    cookies=cookies,
    headers=headers,
).text
Decrypt=execjs.compile(open('rongzi.js','r',encoding='utf-8').read()).call('Decrypt',response)
print(Decrypt)