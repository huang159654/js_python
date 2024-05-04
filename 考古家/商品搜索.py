import json
import pprint

import execjs
import requests

headers = {
    'authority': 'service.kaogujia.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJQeEs4RUQwS3FVcUdxYXBjS0tka1FRIiwic2lkIjoiNTgzMDI2OCIsImF1ZCI6IjEwMDAiLCJpc3MiOiJrYW9ndWppYS5jb20iLCJ0eXAiOiIxIiwiYndlIjoiMCIsIm5iZiI6MTY4NTcxNTUyNywiZXhwIjoxNjg4MzA3NTI3LCJpYXQiOjE2ODU3MTU1Mjd9.4Macm_1Clehv-0-THzifP7hJNzQkYqAvRuut2pcgRgA',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.kaogujia.com',
    'pragma': 'no-cache',
    'referer': 'https://www.kaogujia.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'version_code': '3.1',
}

params = {
    'limit': '50',
    'page': '2',
    'sort_field': 'sales',
    'sort': '0',
}

json_data = {
    'keyword': '女装',
    'lv1': [1,],
    'market_filter': {'type': 0,},
    'period': 1,
}

response = requests.post('https://service.kaogujia.com/api/sku/search', params=params, headers=headers, json=json_data).json()
da=response['data']
# list_data=execjs.compile(open('vgd.js', 'r', encoding='utf-8').read()).call('decrypt', da)
# # print(list_data)
# json_obj = json.loads(list_data)
# json_data=json_obj['items']
# for i in json_data:
#     # pprint.pprint(i)
#
#     json_product_id=i['product_id']
#     json_url='https://www.kaogujia.com/productDetails/productOverview?producId='+json_product_id
#     json_title = i['title']#衣服名字
#     json_day30_sales = i['day30_sales']  # 商品销量
#     sa = i['price']  # 商品价格
#     json_price = '{:.2f}'.format(float(sa/100))
#     print(json_title,json_day30_sales,json_price,json_url)
