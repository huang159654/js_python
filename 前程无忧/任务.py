import csv
import re
import time

import execjs
import requests
f = open('前程无忧.csv', mode='a', encoding='utf_8_sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位名',
    '单位名字',
    '薪资',


])
csv_writer.writeheader()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'guid=f08c90609c2b2744577dbe77a8e8cb8f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22f08c90609c2b2744577dbe77a8e8cb8f%22%2C%22first_id%22%3A%22187e5510add637-0be99879ecc19-26031851-921600-187e5510adedb8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3ZTU1MTBhZGQ2MzctMGJlOTk4NzllY2MxOS0yNjAzMTg1MS05MjE2MDAtMTg3ZTU1MTBhZGVkYjgiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJmMDhjOTA2MDljMmIyNzQ0NTc3ZGJlNzdhOGU4Y2I4ZiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22f08c90609c2b2744577dbe77a8e8cb8f%22%7D%2C%22%24device_id%22%3A%22187e5510add637-0be99879ecc19-26031851-921600-187e5510adedb8%22%7D; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; slife=lowbrowser%3Dnot%26%7C%26; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaiduyj_42422%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIwXzEuaHRtbD9mcm9tPWJhaWR1YWQmcGFydG5lcj1zZW1fcGNiYWlkdXlqXzQyNDIy%2526k%253Ddde303f5d38e50b55f2689d4327c48d0%2526bd_vid%253D12624840181234531309%26%7C%26; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1684165741,1684490870,1684824510,1685890603; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1685890603; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=ac11000116858945985878184e00cf847126e4564640b2f8b5044d7b60c674; acw_sc__v3=647cb5c964a8ab0f56d9804c7d896be90d3aeeb2; acw_sc__v2=647cb68d90ec441a29430a23945b22ce7a3a7e77; JSESSIONID=54C48DB6C8C0D13273D78BE4942FE2CE; ssxmod_itna=eqxtqUxjxfEDXDnQzqa2xRxQTow5GK9RRfDBkGgxiNDnD8x7YDvzGw3DGgxiKZzQnaD2ohkfnkyoeVbEWH3hv+RqoGLDmKDy9nMxeDxrq0rD74irDDxD3Db8dDSDWKD9D0+8BnLuKGWDm+8DWPDYxDrfrKDRxi7DDvdOx07DQv85Ic+u=OCkCYxfxG1a40HQWftfZAEAfTz5/oxDz4ODlI6DCF1uEyFT4Gd66v1DSTevnTeN0wbN0i3kebKrAuK3jlewnu4auuDOmGtS00KQlPPLihtDDcDSixxaGGDD; ssxmod_itna2=eqxtqUxjxfEDXDnQzqa2xRxQTow5GK9RRD8umxiIQD/KWrWxFo3qDIOXR+AFGFAZk0Qaf8pkBQdDwGG2j=fUE7K+=3itdy2sre8OF9skiQkAg4DyeglGQSFH17hBxh5mISGuaczVKoERK9=BOTa7bqDczhB9sDrGkgjvOVDyDyDnCI=KWVWpdm1AaDoWk+bmbYeEk2E7WkAPrYm8rrcPrgBbtnfcAQoAObcSiKfGN3reX5bu+PNDm3gcbj9kEx6m1erWwkaB6MrwzLE=GIqeWmVwS9acSXMzBk+/NIc1Suu/yMcK/MVX9ioT2N4tipnL2AL6gfGg3cDLyld80GsrYHAf90fQtqIxfbEAxKRH1ISB6s7b4/r21InAbHt3MO546Xu6RR1Tfpu9Q3FFuICKErucoe41RcEfVE38BrpF0Egdxc2sPcKIPESip1c5babfeYRa7x9jOxTDG29DoI0DzxrWxq8uKbDrWGIRW=WDPNiWU2=Wwm/itfdPOudSaQYe4+9bBG4YrkHbQGTO+it7DRQCr3rWFW1KrzhQdICvPqKNQ4Rre3Gv2rFmeQFiWiixQqq4rITd=mMpwCempmR=vgZPD08DiQ=1wAayHjx5B5meA4ip3bDFGmECe4nyAVjiBwkeY6vhLIo6dqm7GHQkjMBHQ1xD',
    'From-Domain': '51job_web',
    'Pragma': 'no-cache',
    'Referer': 'https://we.51job.com/pc/search?keyword=&searchType=2&sortType=0&metro=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'account-id': '',
    'partner': 'sem_pcbaiduyj_42422',
    'property': '%7B%22partner%22%3A%22sem_pcbaiduyj_42422%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3Fkeyword%3D%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    #'sign': ,
    'user-token': '',
    'uuid': 'f08c90609c2b2744577dbe77a8e8cb8f',
}
response = requests.get('https://we.51job.com/api/job/search-pc',headers=headers).text
arg1=re.findall("arg1='(.*?)'",response)[0]
# print(arg1)
sc__v2=execjs.compile(open('sign.js', 'r', encoding='utf-8').read()).call('main123', arg1)
cookies = {
    'guid': 'd5d2064dc2da5949480bdfe35497d2b8',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22d5d2064dc2da5949480bdfe35497d2b8%22%2C%22first_id%22%3A%2218887ba06b6d93-0be196ca697d818-26031a51-921600-18887ba06b7ffb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4ODdiYTA2YjZkOTMtMGJlMTk2Y2E2OTdkODE4LTI2MDMxYTUxLTkyMTYwMC0xODg4N2JhMDZiN2ZmYiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6ImQ1ZDIwNjRkYzJkYTU5NDk0ODBiZGZlMzU0OTdkMmI4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22d5d2064dc2da5949480bdfe35497d2b8%22%7D%2C%22%24device_id%22%3A%2218887ba06b6d93-0be196ca697d818-26031a51-921600-18887ba06b7ffb%22%7D',
    'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    'privacy': '1687407293',
    'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1685904296,1687178965,1687407294',
    'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1687408536',
    'search': 'jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%F3%BC%C6python%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%F3%BC%C6python%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%F3%BC%C6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B9%A4%B3%CC%C9%F3%BC%C6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA01%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%F3%BC%C6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
    'JSESSIONID': '15903D48E88EF8B4E50B92F5E00D5F99',
    'ssxmod_itna': 'eqRx9D0DBQ0QYiKGHD8KRhrxUhUADcj=QGWEcGx0yDAeGzDAxn40iDto=TE74Px82KaxT=DbNak/24o4+CWZnW3DHxY=DUc7+4oD4SKGwD0eG+DD4DWDmWFDnxAQDjxGPnUpNH=DEDm48DWPDYxDrAoKDRxi7DDHQHx07DQ58Pza+2Pgk=WYoAxG1T40HGQ34AcYEI+01P9oo/E+7DlK6DC9C2hHFr4GdLp51/oxeWA+2bBwHG0bqqADxznGxWGxY7y0udp4e5EiqG7DeKBRP5hhRDDaovsxeiYD',
    'ssxmod_itna2': 'eqRx9D0DBQ0QYiKGHD8KRhrxUhUADcj=QGWEcDnF3eh4Ds=eYDLQirQ7kDOYbDSPGFnaqKr8cRQWv0FKj=APT8t6PnfbqXfawDa1kDTMYekMK89CgujcgIC88IV+QjlyRHwNUcl4k7U/Ai0wYQiqkkY4oQ2Ze4fK53RxPjUqErQhYWvdPWTtLlXiTnYgQP0mSuQWO1aaNfY8fTF=p=F7E4aOH4oXBw47S4=MUby/UZ7Cc8ADk=yWVdiENLtuUdSHs/XLsZr1BF2+hu8aPTEO5uFaV8BuNq4jDvIKmHa3tI9unjMpfONncLgojCZXgeeyrPS0Pu20PFjcZvxfiScD5t5l=QYWDfBm=iqqAX8YIInDujxYl4uieiGIDrePiIWDG28G4YD/Yx=Dx4tnDerIK0d3h=GD3yoYU9N6Atp+KfbqnhPS2iLh=oDZQ056gDioYREtU8FVY5+hbm+ayid5G4Q3YUOQD58Ev8xgHY3oA0n4rPaDQ8S=9kdciavqeW4eWGb+34efth0hdf+xo4D08DiQh+DincMSDIIRYnGCtwhfOqebTu2Kd+VfG6nBYQn=GDU0T09ch82KvGh8DIfg5ibVtWYYD===',
    'acw_tc': 'ac11000116874247262562752e00d2861923ed1172cf39e1e86f0dae9747b9',
    'acw_sc__v2': sc__v2,
}
for pageNum in range(10,11):
    print(f'正在下载{pageNum}页')
    params = {
        'api_key': '51job',
        'timestamp': '1687424725',
        'keyword': '会计python',
        'searchType': '2',
        'function': '',
        'industry': '',
        'jobArea': '000000',
        'jobArea2': '',
        'landmark': '',
        'metro': '',
        'salary': '',
        'workYear': '',
        'degree': '',
        'companyType': '',
        'companySize': '',
        'jobType': '',
        'issueDate': '',
        'sortType': '0',
        'pageNum': pageNum,
        'requestId': '9c4a5508c305ba4b6f5246cc126316c1',
        'pageSize': '20',
        'source': '1',
        'accountId': '',
        'pageCode': 'sou|sou|soulb',
    }
    time.sleep(2)
    response1 = requests.get('https://we.51job.com/api/job/search-pc', params=params, cookies=cookies, headers=headers).json()
    data=response1.get('resultbody').get('job').get('items')
    for list in data:
        try:
            url_jobHref=list.get('jobName')#职位名
            url_fullCompanyName = list.get('fullCompanyName')  #单位名字
            url_provideSalaryString = list.get('provideSalaryString')  # 薪资
            dit = {
                '职位名': url_jobHref,
                '单位名字': url_fullCompanyName,
                '薪资': url_provideSalaryString,
            }
            csv_writer.writerow(dit)
            print(url_jobHref,url_fullCompanyName,url_provideSalaryString)
        except Exception as e:
            e
