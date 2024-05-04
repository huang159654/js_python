import requests

cookies = {
    'bidguid': 'aa3e32cf-4983-4d6f-95c6-ed205223ae5a',
    'Hm_lvt_9954aa2d605277c3e24cb76809e2f856': '1688393100,1688461791,1690813237',
    'Hm_lvt_4c05dfde8a8c772de99bf56bbd4964b8': '1690816659',
    'Hm_lpvt_4c05dfde8a8c772de99bf56bbd4964b8': '1690816659',
    'ASP.NET_SessionId': 'ivbk242fcz0wxljopxl23xkh',
    '__51cke__': '',
    'Hm_lpvt_9954aa2d605277c3e24cb76809e2f856': '1690816887',
    '__tins__1307476': '%7B%22sid%22%3A%201690816798380%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201690818687362%7D',
    '__51laig__': '5',
}

headers = {
    'authority': 'www.bidcenter.com.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'bidguid=aa3e32cf-4983-4d6f-95c6-ed205223ae5a; Hm_lvt_9954aa2d605277c3e24cb76809e2f856=1688393100,1688461791,1690813237; Hm_lvt_4c05dfde8a8c772de99bf56bbd4964b8=1690816659; Hm_lpvt_4c05dfde8a8c772de99bf56bbd4964b8=1690816659; ASP.NET_SessionId=ivbk242fcz0wxljopxl23xkh; __51cke__=; Hm_lpvt_9954aa2d605277c3e24cb76809e2f856=1690816887; __tins__1307476=%7B%22sid%22%3A%201690816798380%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201690818687362%7D; __51laig__=5',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = {
    'keywords': '钢结构',
}

response = requests.get('https://www.bidcenter.com.cn/xiangmu', params=params, cookies=cookies, headers=headers).text
print(response)