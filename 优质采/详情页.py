import re

import execjs
import requests

cookies = {
    '_qddac': '3-3-1.3b8zjr.aqbqql.lj2uwbt7',
    'ASP.NET_SessionId': 'tbjwazglkrt2yyzrl4xgqqli',
    'Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da': '1687179139',
    '__root_domain_v': '.youzhicai.com',
    '_qddaz': 'QD.761584385103191',
    '_qdda': '3-1.3b8zjr',
    '_qddab': '3-aqbqql.lj2uwbt7',
    'isPopUp': '1',
    'Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da': '1687179703',
   # 'spvrscode': '18438a2c05a6e0a93d619affe55594cd0a2479a1f8fd13855c41946e6584ec20b4577823280064b4cee5ff7fa7e44194deee36b75fb42f75dbeebf99b24a6d0fa4934cdb9a333ed9646937c6a4ba4dfbe9178e0864c04982a6edf4a60e3e886d19cb8cba7fe6403e82f09340be96dec0218fd5a5b0e125d8a1b57b83015f1eb1106d3af8873250a7',
}
headers = {
    'authority': 'www.youzhicai.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_qddac=3-3-1.3b8zjr.aqbqql.lj2uwbt7; ASP.NET_SessionId=tbjwazglkrt2yyzrl4xgqqli; Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da=1687179139; __root_domain_v=.youzhicai.com; _qddaz=QD.761584385103191; _qdda=3-1.3b8zjr; _qddab=3-aqbqql.lj2uwbt7; isPopUp=1; Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da=1687179703; spvrscode=18438a2c05a6e0a93d619affe55594cd0a2479a1f8fd13855c41946e6584ec20b4577823280064b4cee5ff7fa7e44194deee36b75fb42f75dbeebf99b24a6d0fa4934cdb9a333ed9646937c6a4ba4dfbe9178e0864c04982a6edf4a60e3e886d19cb8cba7fe6403e82f09340be96dec0218fd5a5b0e125d8a1b57b83015f1eb1106d3af8873250a7',
    'pragma': 'no-cache',
    'referer': 'https://www.youzhicai.com/nd/f0498e1f-22b1-49ed-b4b7-8bf2f4060850-1.html',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
response = requests.get('https://www.youzhicai.com/nd/f0498e1f-22b1-49ed-b4b7-8bf2f4060850-1.html', cookies=cookies, headers=headers).text
# print(response)
response =re.sub('\s','',response)
var_a =re.findall("vara='(.*?)'",response)[0]
var_b =re.findall("varb='(.*?)';",response)[0]
cookies123=execjs.compile(open('./dome.js', 'r', encoding='utf-8').read()).call('mian_123', var_a, var_b)
# print(cookies123)
cookies_1 = {
    'ASP.NET_SessionId': 'tbjwazglkrt2yyzrl4xgqqli',
    'spvrscode': cookies123,
}
response_1 = requests.get('https://www.youzhicai.com/nd/f0498e1f-22b1-49ed-b4b7-8bf2f4060850-1.html', cookies=cookies_1, headers=headers).text
print(response_1)