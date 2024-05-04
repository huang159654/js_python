import execjs
import requests
mcode = execjs.compile(open('demo_1.js', 'r', encoding='utf-8').read()).call('getResCode')
# print(mcode)
cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1686979572',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1686981276',
    'JSESSIONID': 'CE7E46E1C685A11EDA3645188ADAB1F3',
}

headers = {
    'Accept': '*/*',
    'Accept-EncKey': mcode,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686979572; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686981276; JSESSIONID=CE7E46E1C685A11EDA3645188ADAB1F3',
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
    'scode': '399001',
    'market': '012002',
    'orgid': 'jysz0000001',
    'sdate': '2022-06-17',
    'edate': '2023-06-17',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1095', cookies=cookies, headers=headers, data=data).json()
print(response)