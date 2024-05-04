import requests

import execjs

json_data_js = execjs.compile(open('xiniu.js', 'r', encoding='utf-8').read()).call('main')
# print(json_data_js)
cookies = {
    'btoken': 'BV7TLGPPIKUZBFGCJ3641G5D6F421AF9',
    'hy_data_202'
    '0_id': '18718ee1ea1278-08da4a831b97a2-26031851-921600-18718ee1ea2a75',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218718ee1ea1278-08da4a831b97a2-26031851-921600-18718ee1ea2a75%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218718ee1ea1278-08da4a831b97a2-26031851-921600-18718ee1ea2a75%22%7D',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1679750471,1679766274',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1679777006',
}
headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'btoken=BV7TLGPPIKUZBFGCJ3641G5D6F421AF9; hy_data_2020_id=18718ee1ea1278-08da4a831b97a2-26031851-921600-18718ee1ea2a75; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218718ee1ea1278-08da4a831b97a2-26031851-921600-18718ee1ea2a75%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218718ee1ea1278-08da4a831b97a2-26031851-921600-18718ee1ea2a75%22%7D; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1679750471,1679766274; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1679777006',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

json_data = {
    'payload': json_data_js['payload'],
    'sig': json_data_js['sig'],
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
d = response['d']
# print(d)
Decrypting_data = execjs.compile(open('xiniu.js', 'r', encoding='utf-8').read()).call('mian', d)
print(Decrypting_data)
