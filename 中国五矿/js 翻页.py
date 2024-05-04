import execjs
import requests

cookies = {
    '__jsluid_s': '53ca8c1a71928cc3acca8c570221526a',
    'SUNWAY-ESCM-COOKIE': '6ad44501-d89b-465c-a829-cb80d5dc2e84',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': '__jsluid_s=53ca8c1a71928cc3acca8c570221526a; SUNWAY-ESCM-COOKIE=6ad44501-d89b-465c-a829-cb80d5dc2e84',
    'Origin': 'https://ec.minmetals.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info/?tabIndex=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post('https://ec.minmetals.com.cn/open/homepage/public', cookies=cookies, headers=headers).text
# print(response)
with open("./wuk.js", "r", encoding='utf-8') as f:
    js_code = f.read()
    # 执行JavaScript代得
ctx = execjs.compile(js_code)
# print(ctx)
for i in range(1,6):
    result = ctx.call("mian123", response, i)
    json_data = {
        'param': result,
    }

    response_1 = requests.post(
        'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()
    print(response_1)
