import re

import execjs
import requests

cookies = {
    'ASP.NET_SessionId': 'ugelr0kks0eu5suu3hrohpim',
    'Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da': '1684385103',
    '__root_domain_v': '.youzhicai.com',
    '_qddaz': 'QD.761584385103191',
    'isPopUp': '1',
    '_qdda': '3-1.1',
    '_qddab': '3-pwm6jt.lhwy4jru',
    'Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da': '1684645031',
}

headers = {
    'authority': 'www.youzhicai.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'ASP.NET_SessionId=ugelr0kks0eu5suu3hrohpim; Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da=1684385103; __root_domain_v=.youzhicai.com; _qddaz=QD.761584385103191; isPopUp=1; _qdda=3-1.1; _qddab=3-pwm6jt.lhwy4jru; Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da=1684645031',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

response = requests.get('https://www.youzhicai.com/sn/150.html', cookies=cookies, headers=headers).text
# print(response)
response =re.sub('\s','',response)
var_a =re.findall("vara='(.*?)'",response)[0]
var_b =re.findall("varb='(.*?)';",response)[0]
cookies123=execjs.compile(open('./dome.js', 'r', encoding='utf-8').read()).call('mian_123', var_a, var_b)
# print(cookies123)
cookies = {
    'ASP.NET_SessionId': 'ugelr0kks0eu5suu3hrohpim',
    'spvrscode': cookies123,
}
response_1 = requests.get('https://www.youzhicai.com/sn/150.html', cookies=cookies, headers=headers).text
print(response_1)