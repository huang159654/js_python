import re
import execjs
import requests
url='https://www.cnpcbidding.com/cms/css/bj.css'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'MACHINE_CODE': '1692928943700',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnpcbidding.com/?',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
resp=requests.get(url,headers=headers).text
res=re.findall('url\(data:image/png;base64,(.*?)\)',resp,re.S)
logo1=res[0]
# print(logo1)
page=1 #页数
data=execjs.compile(open('demo.js','r',encoding='utf-8').read()).call('jiami',logo1,page)
logo2=res[1]
headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'www.cnpcbidding.com',
    'MACHINE_CODE': '1692928943700',
    'Origin': 'https://www.cnpcbidding.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnpcbidding.com/?',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.post('https://www.cnpcbidding.com/cms/article/page', headers=headers1, data=data).json()
jiemi=execjs.compile(open('demo.js','r',encoding='utf-8').read()).call('jiemi',logo2,response)
print(jiemi)

