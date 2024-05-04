import execjs
import requests

cookies = {
    'NMTID': '00OvgifSTg28e9wkUzjrmZQ7apJK-cAAAGJbpduUA',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': '1fd4f9281b27cd6615bd4865a8aa1c0e,1689777560956',
    '_ntes_nuid': '1fd4f9281b27cd6615bd4865a8aa1c0e',
    'WEVNSM': '1.0.0',
    'WNMCID': 'xoftem.1689777562366.01.0',
    'WM_TID': 'FsHBlJ%2FtdRdBFBFRVFaA12n4wno7tQEs',
    'ntes_utid': 'tid._.KbDg7rdFeDFBBgEUEVPB1ynpw26VQiT1._.0',
    'sDeviceId': 'YD-87Q7iAnawXVEA0QRBFLBl3zski%2BQU2Hw',
    'JSESSIONID-WYYY': 'iW4gXOCI7IQSu%2BWCoCx7lp5qqBoCKwRshRRKXJi%5C8%5C1GWhAPg%2B6PD3%2F9qoF6c%2B%5Cw6Mfq2eAIMw5tgUV5JKPlXjmZp%5C%2Bd0r720yvxXdgnxtUF%5C%2FrlbsrgujOVoRVse%2Bx0Ya6Ig1q%5CIaOQbIoEenNbN3QsQiVTI6Xu9WRsZteXsF%5C%5Crvtk%3A1690811767531',
    'WM_NI': 'NLsf4NqLLn4yoC4YZxsQync%2FOoQEgj9cctb3j5VLiEprgstIll3qyX5i2WOqisFFYtTzEEmArIwwMpMRiHLnqlbBd03CA6OYlKK13WZjy%2BfZR9YJFUqO6q3vdK8BA5Yndzc%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eea3cf6387bd97bbed3988b88fb6d45b968a8eadd43cf7eda4b9d550ab8cc0d7ce2af0fea7c3b92a8e94bd87b746b394848fb773ad9dfcbad974b18fb78fe2258db19fa6e662fbbdad95e139aaeb9aadec4fb4aea994f743b0b4fd92fc54f7b7feb8ce7babad8aa7dc8098a68ba6f04bb297b998d07c8f8ea7a9cf66b3b4aea3e73cf19d8fd7ce53b09585d2b25d9ab6b7cce55292e797abc55fb391fa92b27ea895f8a3c43f9bb2ac9be237e2a3',
    'playerid': '50628268',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'NMTID=00OvgifSTg28e9wkUzjrmZQ7apJK-cAAAGJbpduUA; _iuqxldmzr_=32; _ntes_nnid=1fd4f9281b27cd6615bd4865a8aa1c0e,1689777560956; _ntes_nuid=1fd4f9281b27cd6615bd4865a8aa1c0e; WEVNSM=1.0.0; WNMCID=xoftem.1689777562366.01.0; WM_TID=FsHBlJ%2FtdRdBFBFRVFaA12n4wno7tQEs; ntes_utid=tid._.KbDg7rdFeDFBBgEUEVPB1ynpw26VQiT1._.0; sDeviceId=YD-87Q7iAnawXVEA0QRBFLBl3zski%2BQU2Hw; JSESSIONID-WYYY=iW4gXOCI7IQSu%2BWCoCx7lp5qqBoCKwRshRRKXJi%5C8%5C1GWhAPg%2B6PD3%2F9qoF6c%2B%5Cw6Mfq2eAIMw5tgUV5JKPlXjmZp%5C%2Bd0r720yvxXdgnxtUF%5C%2FrlbsrgujOVoRVse%2Bx0Ya6Ig1q%5CIaOQbIoEenNbN3QsQiVTI6Xu9WRsZteXsF%5C%5Crvtk%3A1690811767531; WM_NI=NLsf4NqLLn4yoC4YZxsQync%2FOoQEgj9cctb3j5VLiEprgstIll3qyX5i2WOqisFFYtTzEEmArIwwMpMRiHLnqlbBd03CA6OYlKK13WZjy%2BfZR9YJFUqO6q3vdK8BA5Yndzc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3cf6387bd97bbed3988b88fb6d45b968a8eadd43cf7eda4b9d550ab8cc0d7ce2af0fea7c3b92a8e94bd87b746b394848fb773ad9dfcbad974b18fb78fe2258db19fa6e662fbbdad95e139aaeb9aadec4fb4aea994f743b0b4fd92fc54f7b7feb8ce7babad8aa7dc8098a68ba6f04bb297b998d07c8f8ea7a9cf66b3b4aea3e73cf19d8fd7ce53b09585d2b25d9ab6b7cce55292e797abc55fb391fa92b27ea895f8a3c43f9bb2ac9be237e2a3; playerid=50628268',
    'nm-gcore-status': '1',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/search/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '',
}

data = {
    'params': 'A6AcPrGE+eCE9cIYkQ23q1kdQ/EuokH8+In6HWpN+v4gWPMXconkwgy54x1TPjdjRxD0fh0RYWvbfSl08PrlIHL/tHE4sRQ5u7PiZ/QdXiIIx0kZPLKpjM/1MzsE8XDMqI56ANZTkkmFJMv48rbN2sZicTOfMF21Lxk7C/1VFZPXGrPEf031hnwBa/hZcpZtpxyu1xd1lnPISBJ6QpgTNE5zPL4XhSGX+++l24XEbXcCgryTEB+/XWAmjFf3RA2IeP1zH1w5ouyDowcx6pQM2A==',
    'encSecKey': 'a9abd4ade6ba13b2b5c2cb78835e2b094dfb55523bd60371a36a8126f307cb57a9671cdc1dc0504797cbe60956e014801415e39b43e1af9023156661f067a30e0fb351f4e35e83786041adfe9deb352228471310b86cbcd0184df1b4e8c7866c4233cd91016ecd008d3a3ef506996653be8087a839a8fe25ae9041fbc65ac348',
}

response = requests.post(
    'https://music.163.com/weapi/cloudsearch/get/web',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
).json()

list=response.get('result').get('songs')
for i in list:
    id=i.get('al').get('id')
    exec_js=execjs.compile(open('./sous.js','r',encoding='utf-8').read()).call('mian',id)
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
        'encSecKey': exec_js['encSecKey'], }

    response = requests.post(
        'https://music.163.com/weapi/song/enhance/player/url/v1',
        params=params,
        headers=headers,
        data=data,
    ).json()
    print(response)
    # data_url = response.get('data')[0].get('url')
    # title = response.get('data')[0].get('id')
    # mp3_url = requests.get(url=data_url, ALL_headers=ALL_headers).content