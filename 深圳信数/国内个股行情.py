import execjs
import requests


mcode = execjs.compile(open('demo_1.js', 'r', encoding='utf-8').read()).call('getResCode')
# print(mcode)
headers = {
    'Accept': '*/*',
    'Accept-EncKey': mcode,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'routeId=.uc2; SID=78aad89b-d0aa-45a0-9a94-44bc25bf2efc; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686930015; JSESSIONID=6F49C0D74B3FE2326E1F925263846B52; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686930044',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'scode': '000001-SZE',
    'sdate': '2022-06-16',
    'edate': '2023-06-16',
    'ctype': '0',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008', headers=headers, data=data).json()
print(response)