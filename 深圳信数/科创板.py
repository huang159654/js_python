import execjs
import requests
mcode = execjs.compile(open('demo_1.js', 'r', encoding='utf-8').read()).call('getResCode')
cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1686979572',
    'JSESSIONID': 'EA438A8B3F719B0DF43F9113116E9F57',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1686982141',
}

headers = {
    'Accept': '*/*',
    'Accept-EncKey': mcode,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686979572; JSESSIONID=EA438A8B3F719B0DF43F9113116E9F57; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686982141',
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

params = {
    'market': '012029',
}

response = requests.post('https://webapi.cninfo.com.cn/api/stock/p_stock2247', params=params, cookies=cookies, headers=headers).json()
print(response)