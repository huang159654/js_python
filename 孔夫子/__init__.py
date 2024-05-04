import time
from urllib import parse
import requests
import execjs
key=input('请输入书名ID或书名:')
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'randomcodekey=srck27194232924546frz889; randomcodesign=WV38D2INQSOK24CbwXvwTLDQVEeT4oOTUCGvtpF1ru3sevnxggtVxHbBjTJ7FwtJZy6j1iigpEkQJiuDBe7Udg%3D%3D; randomcode=195033171573; acw_tc=276077c016904578039184801e17b71cf155214abb8d211875188c6ff57a89; TY_SESSION_ID=719b51d7-a3a3-4bfe-b730-8cf8fdf3f44a; PHPSESSID=jsem3nbeqp148eml4q5rh41232; shoppingCartSessionId=a8774c41608a7c34aa80d678bf646780; reciever_area=1006000000; kfz-tid=67fb6e66280aca506264d035891cba2d',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'key': key,
    'status': '0',
    '_stpmt': 'eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9',
    'pagenum': '3',
    'ajaxdata': '1',
}

response = requests.get('https://search.kongfz.com/product_result/', params=params, headers=headers)
randomcode=response.cookies['randomcode']
randomcodekey=response.cookies['randomcodekey']
acw_tc=response.cookies['acw_tc']
# print(randomcode,randomcodekey,acw_tc)
i=3#页数
t=int(time.time()*1000)
url=f'https://search.kongfz.com/product_result/?key={key}&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9&pagenum={i}&ajaxdata=1&type=1&_={t}'
data=open('d.js', 'r', encoding='utf-8').read()
list =execjs.compile(data).call('rqEncrypt',randomcode)
print(list)
randomcodesign=parse.quote(list[0])
# print(randomcodesign) #这个
# TY_SESSION_ID=list[1]
headers['cookie']=f'randomcodekey={randomcodekey}; randomcode={randomcode}; randomcodesign={randomcodesign};acw_tc={acw_tc}; '
headers['X-Tingyun-Id']=f'OHEPtRD8z8s;r={t%1000000000}'
# pprint.pprint(ALL_headers)
resp=requests.get(url,headers=headers).json()
print(resp)