#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/9/8 21:55
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re

import requests

cookies = {
    '_csrfToken': 'abJaIcGDLtumToPWEy9mH3JZM6AEO89UOUbqkBP5',
    'newstatisticUUID': '1694176725_506594482',
    '_yep_uuid': 'cd4493e9-339d-34a6-cb95-d949f1c13290',
    'Hm_lvt_f00f67093ce2f38f215010b699629083': '1694176715',
    'fu': '531040169',
    '_gid': 'GA1.2.1811286607.1694176715',
    'e2': '',
    'e1': '%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A15%22%7D',
    'supportwebp': 'true',
    'supportWebp': 'true',
    'trkf': '1',
    'ywguid': '120030948752',
    'ywopenid': '2B813868967939285C77CC4E4D68700B',
    'ywkey': 'ywll63KbMQav',
    'Hm_lpvt_f00f67093ce2f38f215010b699629083': '1694177334',
    '_ga': 'GA1.1.1908313213.1694176715',
    '_ga_FZMMH98S83': 'GS1.1.1694176715.1.1.1694177485.0.0.0',
    '_ga_PFYW0QLV3P': 'GS1.1.1694176715.1.1.1694177485.0.0.0',
    'traffic_utm_referer': 'https%3A//www.baidu.com/link',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '    newstatisticUUID=1694181815_1597076664; fu=1598816441; Hm_lvt_f00f67093ce2f38f215010b699629083=1694181806; _gid=GA1.2.1062149438.1694181806; supportWebp=true; supportwebp=true; trkf=1; _yep_uuid=2c7b5fd0-4ea3-a51d-0119-6e93ed6f7ed8; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%7D; _csrfToken=8b6c0584-fabf-4874-b784-c869b82caf32; ywguid=120030948752; ywkey=ywTRGTyZBr6W; ywopenid=2B813868967939285C77CC4E4D68700B; traffic_utm_referer=https%3A%2F%2Fwww.baidu.com%2Flink; Hm_lpvt_f00f67093ce2f38f215010b699629083=1694352903; _ga=GA1.1.1569780973.1694181806; _ga_FZMMH98S83=GS1.1.1694350502.6.1.1694352967.0.0.0; _ga_PFYW0QLV3P=GS1.1.1694350501.6.1.1694352967.0.0.0',
    'Pragma': 'no-cache',
    'Referer': 'https://www.qidian.com/book/1030870265/',#这个是这边书的目录网址
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Yuew-sign': '81f269076b1b4693d401efc5c7492fae',
    'X-Yuew-time': '1694177486',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    '_csrfToken': 'abJaIcGDLtumToPWEy9mH3JZM6AEO89UOUbqkBP5',
    'bookId': '1030870265',#这个是这本书的ID
}
response = requests.get('https://www.qidian.com/ajax/book/category', params=params, cookies=cookies, headers=headers)
response.encoding=response.apparent_encoding  #这个是自动转换编码
list=response.json().get('data').get('vs')
ds=[]
id_lst=[]
nema=[]
for list_dat in list:
    d=list_dat.get('cs')
    for i in d:
        name=i.get('cN')
        url_id=i.get('id')
        dsd=name+'_'+str(url_id)
        ds.append(dsd)
        # print(name,url_id) #这里打印全部书籍章节，和章节id
target = '第九百三十二章 维恩神战！_761551083' # 这里是你想要从哪里开始下载，719729994这个是这个章节的ID
result = ds[ds.index(target):]
for resul in result:
    fi=resul.split('_')[0]
    di_s = resul.split('_')[1]
    # print(di_s)
    id_lst.append(di_s)
    nema.append(fi)
for dia in id_lst:
    response_1 = requests.get(f'https://www.qidian.com/chapter/1030870265/{dia}/', headers=headers, cookies=cookies).text
    print(response_1)
    break
    #     content = re.findall('\<p\>\　\　(.*?)\<\/p\>', response_1)  # 内容
    #     print(content)
    #     with open(f'{dau}.txt', 'w', encoding='utf-8') as f:  # 这里是保存文件
    #         for data in content:
    #             f.write(data + '\n')  # 添加‘\n’用于换行
    # print('下载完毕!', dau)
