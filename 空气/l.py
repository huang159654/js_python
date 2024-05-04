import requests

cookies = {
    'Hm_lvt_6088e7f72f5a363447d4bafe03026db8': '1688551610,1689763966,1690632032',
    'Hm_lpvt_6088e7f72f5a363447d4bafe03026db8': '1690809352',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_6088e7f72f5a363447d4bafe03026db8=1688551610,1689763966,1690632032; Hm_lpvt_6088e7f72f5a363447d4bafe03026db8=1690809352',
    'Pragma': 'no-cache',
    'Referer': 'http://www.aqistudy.cn/historydata/daydata.php?city=%E5%A4%A7%E8%BF%9E&month=201312',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://www.aqistudy.cn/historydata/resource/highcharts/highcharts.js',
    cookies=cookies,
    headers=headers,
    verify=False,
).text
with open('d.js','w',encoding='utf-8')as f:
    f.write(response)
