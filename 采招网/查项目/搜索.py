
import json
import pprint

import requests
import execjs
keywords=input('请输入查询名字:')
headers = {
    'authority': 'interface.bidcenter.com.cn',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://search.bidcenter.com.cn',
    'pragma': 'no-cache',
    'referer': 'https://search.bidcenter.com.cn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
data = {
    'from': '6137',
    'guid': 'aa3e32cf-4983-4d6f-95c6-ed205223ae5a',
    'location': '6138',
    'token': '',
    'next_token': '',
    'keywords': keywords,
    'mod': '0',
    'page': '1',
}
response = requests.post('https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx', headers=headers, data=data).text
list=execjs.compile(open('dome.js', 'r', encoding='utf-8').read()).call('AESDecrypt', response)
list=json.loads((list))
listData=list.get('other2').get('listData')
pprint.pprint(listData)