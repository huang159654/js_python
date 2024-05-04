import base64
import time
from urllib import parse
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import requests



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
# params = {
#     'key': key,
#     'status': '0',
#     '_stpmt': 'eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9',
#     'pagenum': '1',
#     'ajaxdata': '1',
#     'hasStock': '1',
#     'type': '1',
#     'area': '1006000000',
#     '_': '1712553627880',
# }
def get_randomcodesign(randomcode):
    publickey = "-----BEGIN PUBLIC KEY-----\n" + "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMiU6MWuUemPQkPAZSfYUBD6qfgQfM/jY3OEBbdNlOm0SBjX4Z1GMSg0Jhk70NQlxNfrbz4oN0A+jVhoH7gEyY8CAwEAAQ==" + "\n-----END PUBLIC KEY-----"
    key = RSA.import_key(publickey) #这个你是从哪里看到RSA的，从网页哪里分析出来的
    cipher = PKCS1_v1_5.new(key)#PKCS1_v1_5这个是啥
    encode_rsa_data = cipher.encrypt(str(randomcode).encode())
    b64_encode_data = base64.b64encode(encode_rsa_data)
    randomcode = b64_encode_data.decode()
    randomcodesign = parse.quote(randomcode)
    print("randomcodesign = " + randomcodesign)
    return randomcodesign

response = requests.get('https://search.kongfz.com/product_result/', params=params, headers=headers)
print(response.cookies)
# randomcode=response.cookies['randomcode']
# print(randomcode)
# randomcodekey=response.cookies['randomcodekey']
# acw_tc=response.cookies['acw_tc']
# randomcodesign = get_randomcodesign(f'{randomcode}')
# # print(randomcode,randomcodekey,acw_tc)# ou
# i=1 #页数
# while True:
#     if i < 4:
#         t=int(time.time()*1000)
#         url=f'https://search.kongfz.com/product_result/?key={key}&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9&pagenum={i}&ajaxdata=1&type=1&_={t}'
#         # TY_SESSION_ID=list[1]
#         headers['cookie']=f'randomcodekey={randomcodekey}; randomcode={randomcode}; randomcodesign={randomcodesign};acw_tc={acw_tc}; '
#         headers['X-Tingyun-Id']=f'OHEPtRD8z8s;r={t%1000000000}'
#         # pprint.pprint(ALL_headers)
#         resp=requests.get(url,headers=headers)
#         randomcode = resp.cookies['randomcode']  # 重新获取服务器返回的randomcode
#         randomcodesign = get_randomcodesign(f'{randomcode}') # 生成对应新的randomcodesign
#         #嗯，你现在都不怎么扣代码是吗？没有呀，怎么容易怎么来，我一般都是能优化就优化，可是我都是扣js从来没有用python搞过这些
#         # 这么说吧，哪个容易拿，就先拿哪个，但是你扣了这段js，你去读这段代码做了什么，这是逆向一定要学的，总不可能不知道代码做了啥就去搞，
#         # 知道它做了什么，你发现可以用python还原，你就去尝试还原，能python最好是python，如果做爬虫程序，后面也要讲效率
#         #是的··现在好多程序都是用python来实现了，很少去扣，都是扣完就用python实现，然后封装，你会封装程序不
#         # 这个不难的，随便百度就可以了，打包成exe。主要是为了锻炼技术，现在最多的是自动化，什么扣js，都是浪费时间。很多自动化加拦截监听功能，容易得一b
#         # 直接调用js,扣都不用扣,自动化我是真的不知道该学那些,很多大佬说现在大厂都禁止自动化,因为无脑呀,自动化没什么技术含量,除非你是开发自动化的,
#         # 所以呀，还是得提升技术，现在好多大厂的js都开源了，像XB都开源了，开不开无所谓了
#         print(resp.json())
#         i += 1
#         time.sleep(2)
#     else:
#         break
# 9787570801701    'IPDrcahpG4k4Nx4H1/biRwL2M2gADQXSIU77grrUWOn03CphBQcRry5GeIGZo91xRtBu3LWCUR+M87QGMSz6Hw=='
#                  'ZhXDOzCUGTYsggwhmm7XztkiMxcgz8eop31aZ7RWN77L7d3Hy3d42NtMdauvULJwXMPCvw94QGbNsXEbhHGjCw%3D%3D'