import requests

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1685698503,1685946816',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1685957555',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1685698503,1685946816; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1685957555',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://jzsc.mohurd.gov.cn/home', cookies=cookies, headers=headers).text
print(response)