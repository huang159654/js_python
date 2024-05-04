import execjs
import requests
mcode = execjs.compile(open('demo_1.js', 'r', encoding='utf-8').read()).call('getResCode')
cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1686979572',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1686981276',
    'JSESSIONID': 'ED995E56700876EA9CDE282DEE523C5F',
}

headers = {
    'Accept': '*/*',
    'Accept-EncKey': mcode,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686979572; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1686981276; JSESSIONID=ED995E56700876EA9CDE282DEE523C5F',
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
    'tdate': '2023-06-16',
    'market': 'SZE',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007', cookies=cookies, headers=headers, data=data).json()
print(response)