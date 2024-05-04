import requests
import execjs
#切换歌手id在js里面
exec_js=execjs.compile(open('./sous.js','r',encoding='utf-8').read()).call('mian')
headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.898844859.1680955673; Qs_lvt_382223=1680955673; Qs_pv_382223=3675810102444150000; _clck=x2w4wi|1|fal|0; _ga_C6TGHFPQ1H=GS1.1.1680955672.1.1.1680955713.0.0.0; _ntes_nnid=fe289adc13b99dd172ff467e13359b90,1683194131349; _ntes_nuid=fe289adc13b99dd172ff467e13359b90; NMTID=00OgYNvQ68RX_R4y0QVtmhvDqoF7ckAAAGH5jA6mw; WEVNSM=1.0.0; WNMCID=nkthwl.1683194131606.01.0; WM_TID=SHZ6QydQTq5BQUBEQULUL7hpWkBftWWd; JSESSIONID-WYYY=RHUOosZvyd5s%2FdI1rQBnJEmjPmZtRy8iPPE2%2FnQc%5CG2q0519r7AiixiEFDhn1v5W0kBzujHzWRAk29jD7%2Bp%2FfKNXa%2Bx8Dir7Omv3bb4eWYj56EznnniFgiBC20MU6YcJzJiFjTTyyonqENMRhfITnHMGQe9jAd0CVWc5JmY9xVDpgs7T%3A1683987984402; _iuqxldmzr_=33; WM_NI=l2G%2BOTIPGwJWjGsRGzB6G6lxGQLCoX%2BkrJPG0W17T0zoEkKm7abBBTA0rYU%2FKHOCyR2%2B1jPH6rYUBNz2uwfldV8Uwq9YPel63m9Pw%2Bn%2BtmrYnMdxzCebH73Dxf%2B3Rc98djc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee98d666f79bbaa7d54faae78ab7c55f839f8b87c1689786fd87c66ee9aca0b9b82af0fea7c3b92ab0ee89ccce608b908998c95daa99bdb3c67282ea89d7ef74858f84a4ee54e9b5beabd34df489ffd8d73cbab18b8cca67f5bfaea3c16083f0bebad825899881a4fc5af2f5ff8bd344f6ae97b6c146baeebb98e568a88af8b6f67bfb87a086ef3ef1b3f7b1f621aef5bc8ef153ae93ac99f949a7be88d8b250bcbae5d4d169fbe8ac8be237e2a3',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '',
}

data = {
    'params': exec_js['encText'],
    'encSecKey': exec_js['encSecKey'],}

response = requests.post(
    'https://music.163.com/weapi/song/enhance/player/url/v1',
    params=params,
    headers=headers,
    data=data,
).json()
print(response)
data_url=response.get('data')[0].get('url')
title=response.get('data')[0].get('id')
mp3_url=requests.get(url=data_url,headers=headers).content

with open('video\\' + str(title) + '.mp4', mode='wb') as f:
    # 写入数据
    f.write(mp3_url)
print(title)
