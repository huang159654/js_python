
import execjs

import requests
import base64

class BTC_all():
    def __init__(self):
        pass
    def def_base64(self):
        getApiKey=execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('getApiKey')
        # print(getApiKey)
        source = getApiKey
        base64_da=base64.b64encode(source.encode())
        x_apikey=str(base64_da,'utf-8')
        return x_apikey
    def def_headers(self):
        headers = {
            'authority': 'www.oklink.com',
            'accept': 'application/json',
            'accept-language': 'zh-CN',
            'app-type': 'web',
            'cache-control': 'no-cache',
            'cookie': 'aliyungf_tc=3a32fa0a4ea1c43c3260f68ce4f7c3b6c8cd877ee4144b02bdaa4cd2c85ffbfe; locale=zh_CN; _okcoin_legal_currency=CNY; okg.currentMedia=xl; Hm_lvt_5244adb4ce18f1d626ffc94627dd9fd7=1680689836; _monitor_extras={"deviceId":"1yJQfuqt2ZmEAW-DOGd3sL","eventId":6,"sequenceNumber":6}; Hm_lpvt_5244adb4ce18f1d626ffc94627dd9fd7=1680689936',
            'devid': '38c1e443-7981-406d-9f2b-cded6ba06495',
            'pragma': 'no-cache',
            'referer': 'https://www.oklink.com/cn/btc/tx-list?limit=20&pageNum=1',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'x-apikey': self.def_base64(),
            'x-cdn': 'https://static.oklink.com',
            'x-utc': '8',
        }
        return headers
    def def_params(self):
        params = {
            't': '1680689936560',
            'offset': '20',  # 翻页，每一页数据20条从0开始
            'txType': '',
            'limit': '20',
            'sort': '',
        }
        return params
    def def_requests(self):
        response = requests.get(
            'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict',
            params=self.def_params(),
            headers=self.def_headers(),
        ).json()
        print(response)

if __name__=='__main__':
    BTC_all().def_requests()

#
#
#

#
