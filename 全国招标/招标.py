import requests
import execjs

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'http://ctbpsp.com',
    'Referer': 'http://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1',
    headers=headers,
).json()
# if response.status_code==200:
#     print('数据正常！')
# else:
#     response.status_code!= 200,
#     print('请求异常！')
# # print(response)
payload = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('main', response)
print(payload)

