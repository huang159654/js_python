import re

import requests
import execjs

dey = 'https://jobs.51job.com/shanghai-mhq/143513647.html?s=sou_sou_soulb&t=0_0&req=2fe3dc63e6a85fc4dd5cbe3ccbc29c73';
timestamp__1258 = execjs.compile(open('timestamp_1258.js', 'r', encoding='utf-8').read()).call('jiami', dey, )
cookies = {
    'guid': '9779f8affb53edaa5509eb394ac7959d',
    'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    'search': 'jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
    'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1688699836,1690477286,1690535871',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%229779f8affb53edaa5509eb394ac7959d%22%2C%22first_id%22%3A%221892e5a977568c-04e13ce465fa858-26031d51-921600-1892e5a97762e7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fjobs.51job.com%2Fguangzhou-pyq%2F149937027.html%3Fs%3Dsou_sou_soulb%26t%3D0_0%26req%3D2fe3dc63e6a85fc4dd5cbe3ccbc29c73%26timestamp__1258%3DmqUxuDBD2AYWuD05DIA47u7zye4iIND8YeD%26alichlgref%3Dhttps%253A%252F%252Fwe.51job.com%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5MmU1YTk3NzU2OGMtMDRlMTNjZTQ2NWZhODU4LTI2MDMxZDUxLTkyMTYwMC0xODkyZTVhOTc3NjJlNyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6Ijk3NzlmOGFmZmI1M2VkYWE1NTA5ZWIzOTRhYzc5NTlkIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%229779f8affb53edaa5509eb394ac7959d%22%7D%2C%22%24device_id%22%3A%221892e5a977568c-04e13ce465fa858-26031d51-921600-1892e5a97762e7%22%7D',
    'acw_tc': 'ac11000116906371677232635e00d6cc69574be07b5d2b8f4053d5b2b415db',
    'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1690637161',
    'ssxmod_itna': 'QqfhYKDKY5BK0IyxBPGKSg6bXrdvDGuTRnragxDs5eTDSxGKidDqxBnnCa7oGQolriWqaq57RHNa=DRbO4w4aP6ebDHxY=DU=0ymiTDen=D5xGoDPxDeDADYE6DAqiOD7qDdLwHyzkDbxi3LxiaDGeDe6FODY5DhxDC2mPDwx0CLh7FQb5pR=D+5C08D7vpDlPxvI08i+ffoA5+G38GfWKDXhdDvO51M6PpDB+kl1HGTBTPfAleVeKxjQ0xhjD3qliPogq9WwZNqQGqolrqhhhotqDW3i2H5YD==',
    'ssxmod_itna2': 'QqfhYKDKY5BK0IyxBPGKSg6bXrdvDGuTRnra4ikEdNaDlP4YwQ03h5cqaddX59Dn4hkVbWdBw+=it7oR3PoKQ8wHrq8uvikFu1QndUc9FqjBIPPIdl7LtqRK1iv/Gdsf600wKFgiEibXLbkNmYf=Af23jSwiS34dv4k35hk0Bmo3vDSx4zgAisou8W3jBffABFAKPWZDv7SWHp1nq7krkuEFbqhQ1XoyB019wCc5bXZaktrBqYbIwlxFtu2q4mgvE7=jQi+Ms/qCXwMQRZ6kFMakmivZm/6OBZbYeVxtMaXFIA3iYTQdPgYxndIEYgYt4eoRxhQnG503LEaNB5dC+aQhDQ5O7tkm+bQQ7rty2sR2HVMPgEmPgNt83ISPlhpYxInox5OT=D4wRKR015OD523xCDcOWtODRh3e2oaDk1MmrMGrcCT2k1TYjRdFaoTkGU3QfuHFr15dKYEF72z4hTqBPVhoiQPD7QGQD3Kn8WhrAHrn3OCy7IwZfeWBLPiDDjKDedx4D===',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'guid=9779f8affb53edaa5509eb394ac7959d; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1688699836,1690477286,1690535871; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%229779f8affb53edaa5509eb394ac7959d%22%2C%22first_id%22%3A%221892e5a977568c-04e13ce465fa858-26031d51-921600-1892e5a97762e7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fjobs.51job.com%2Fguangzhou-pyq%2F149937027.html%3Fs%3Dsou_sou_soulb%26t%3D0_0%26req%3D2fe3dc63e6a85fc4dd5cbe3ccbc29c73%26timestamp__1258%3DmqUxuDBD2AYWuD05DIA47u7zye4iIND8YeD%26alichlgref%3Dhttps%253A%252F%252Fwe.51job.com%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5MmU1YTk3NzU2OGMtMDRlMTNjZTQ2NWZhODU4LTI2MDMxZDUxLTkyMTYwMC0xODkyZTVhOTc3NjJlNyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6Ijk3NzlmOGFmZmI1M2VkYWE1NTA5ZWIzOTRhYzc5NTlkIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%229779f8affb53edaa5509eb394ac7959d%22%7D%2C%22%24device_id%22%3A%221892e5a977568c-04e13ce465fa858-26031d51-921600-1892e5a97762e7%22%7D; acw_tc=ac11000116906371677232635e00d6cc69574be07b5d2b8f4053d5b2b415db; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1690637161; ssxmod_itna=QqfhYKDKY5BK0IyxBPGKSg6bXrdvDGuTRnragxDs5eTDSxGKidDqxBnnCa7oGQolriWqaq57RHNa=DRbO4w4aP6ebDHxY=DU=0ymiTDen=D5xGoDPxDeDADYE6DAqiOD7qDdLwHyzkDbxi3LxiaDGeDe6FODY5DhxDC2mPDwx0CLh7FQb5pR=D+5C08D7vpDlPxvI08i+ffoA5+G38GfWKDXhdDvO51M6PpDB+kl1HGTBTPfAleVeKxjQ0xhjD3qliPogq9WwZNqQGqolrqhhhotqDW3i2H5YD==; ssxmod_itna2=QqfhYKDKY5BK0IyxBPGKSg6bXrdvDGuTRnra4ikEdNaDlP4YwQ03h5cqaddX59Dn4hkVbWdBw+=it7oR3PoKQ8wHrq8uvikFu1QndUc9FqjBIPPIdl7LtqRK1iv/Gdsf600wKFgiEibXLbkNmYf=Af23jSwiS34dv4k35hk0Bmo3vDSx4zgAisou8W3jBffABFAKPWZDv7SWHp1nq7krkuEFbqhQ1XoyB019wCc5bXZaktrBqYbIwlxFtu2q4mgvE7=jQi+Ms/qCXwMQRZ6kFMakmivZm/6OBZbYeVxtMaXFIA3iYTQdPgYxndIEYgYt4eoRxhQnG503LEaNB5dC+aQhDQ5O7tkm+bQQ7rty2sR2HVMPgEmPgNt83ISPlhpYxInox5OT=D4wRKR015OD523xCDcOWtODRh3e2oaDk1MmrMGrcCT2k1TYjRdFaoTkGU3QfuHFr15dKYEF72z4hTqBPVhoiQPD7QGQD3Kn8WhrAHrn3OCy7IwZfeWBLPiDDjKDedx4D===',
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
    's': 'sou_sou_soulb',
    't': '0_0',
    'req': '2fe3dc63e6a85fc4dd5cbe3ccbc29c73',
    'timestamp__1258': timestamp__1258,
}
response = requests.get('https://jobs.51job.com/shanghai-mhq/143513647.html', params=params, cookies=cookies,
                        headers=headers).text
sign = re.findall('\<input type\=\"hidden\" id\=\"sign\" value\=\"(.*?)\"\>', response)[0]
data = re.findall("<input type=\"hidden\" id=\"data\" value='{\"jobid\":\"(.*?)\",\"usertoken\":false,\"hr\":true}'>",
                  response)[0]
# ALL_headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://jobs.51job.com',
#     'Pragma': 'no-cache',
#     'Referer': 'https://jobs.51job.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
ds = f'data=%7B%22jobid%22%3A%{data}%22%2C%22usertoken%22%3Afalse%2C%22hr%22%3Atrue%7D&sign={sign}'
type__1260 = execjs.compile(open('type__1260.js', 'r', encoding='utf-8').read()).call('dome', ds)
params = {
    'apiversion': '400',
    'module': 'jobinfo',
    'clientid': '000005',
    'type__1260': type__1260,
}
data = {
    'data': '{"jobid":"' + str(data) + '","usertoken":false,"hr":true}',
    'sign': sign,
}
response = requests.post('https://vapi.51job.com/job.php', params=params, data=data).json()
print(response)
