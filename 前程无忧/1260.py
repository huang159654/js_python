import execjs
import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://jobs.51job.com',
    'Pragma': 'no-cache',
    'Referer': 'https://jobs.51job.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
type__1260=execjs.compile(open('type__1260.js', 'r', encoding='utf-8').read()).call('dome', )
# print(type__1260)
params = {
    'apiversion': '400',
    'module': 'jobinfo',
    'clientid': '000005',
    'type__1260': type__1260,
}
data = {
    'data': '{"jobid":"143513647","usertoken":false,"hr":true}',
    'sign': 'e4055a6812422340b74427dd402609b1',
}
'data=%7B%22jobid%22%3A%22149989475%22%2C%22usertoken%22%3Afalse%2C%22hr%22%3Atrue%7D&sign=26499b6fbb789659f228233f4230355e'
response = requests.post('https://vapi.51job.com/job.php', params=params, headers=headers, data=data).json()
print(response)