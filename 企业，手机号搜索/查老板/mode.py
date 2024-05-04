#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/9/25 0:51
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import random
import time

import execjs
import requests
import csv
j=[]

with open('企业名字.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for keyword_1 in reader:
        j.append(keyword_1)



for d in j:
    keyword=d[0]
    hexin_v = execjs.compile(open('demo_v.js', 'r', encoding='utf-8').read()).call('v')
    cookies = {
        'ta_random_userid': 'ihks4vhzmd',
        'u_ukey': 'A10702B8689642C6BE607730E11E6E4A',
        'u_uver': '1.0.0',
        'u_dpass': 'OniAvXFlA5vO470rP1Gipv3pjbPcMsFchObJZGm2hDJtxw%2BE30XuJ3h%2Bq8osd36Z%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D',
        'u_did': '6E05439E1BDE4C7C9B1D8A034248462A',
        'u_ttype': 'WEB',
        'ttype': 'WEB',
        'user': 'MDpteF82OTE5NjYyMzU6Ok5vbmU6NTAwOjcwMTk2NjIzNTo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoxNjo6OjY5MTk2NjIzNToxNjk1NTYxMjQ1Ojo6MTY5NTQ1NDc0MDo2MDQ4MDA6MDoxNDQ4ODZjNzI1NTdmNTI4ZjQ5MDA4YWU1ZWU5ZjVmY2E6ZGVmYXVsdF80OjA%3D',
        'userid': '691966235',
        'u_name': 'mx_691966235',
        'escapename': 'mx_691966235',
        'ticket': 'fb35c47183b8b402f51ad00531c29f88',
        'user_status': '0',
        'utk': '346801c4443efbd1bfd6b2291c07da64',
        'SESSION': 'fe93d68e-eadf-4cd7-8e4a-c01f35d8da5f',
        'JSESSIONID': '973BA68C14133BA9234213FCDFBCD742',
        'jsessionid-yqapp': '0E362BDD7A83D8AECCC0B7C0A1F2095E',
        'v': hexin_v,
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'ta_random_userid=ihks4vhzmd; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=OniAvXFlA5vO470rP1Gipv3pjbPcMsFchObJZGm2hDJtxw%2BE30XuJ3h%2Bq8osd36Z%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D; u_did=6E05439E1BDE4C7C9B1D8A034248462A; u_ttype=WEB; ttype=WEB; user=MDpteF82OTE5NjYyMzU6Ok5vbmU6NTAwOjcwMTk2NjIzNTo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoxNjo6OjY5MTk2NjIzNToxNjk1NTYxMjQ1Ojo6MTY5NTQ1NDc0MDo2MDQ4MDA6MDoxNDQ4ODZjNzI1NTdmNTI4ZjQ5MDA4YWU1ZWU5ZjVmY2E6ZGVmYXVsdF80OjA%3D; userid=691966235; u_name=mx_691966235; escapename=mx_691966235; ticket=fb35c47183b8b402f51ad00531c29f88; user_status=0; utk=346801c4443efbd1bfd6b2291c07da64; SESSION=fe93d68e-eadf-4cd7-8e4a-c01f35d8da5f; JSESSIONID=973BA68C14133BA9234213FCDFBCD742; jsessionid-yqapp=0E362BDD7A83D8AECCC0B7C0A1F2095E; v=AxRWii78DddlgJkbNCNIgdwi5VmDbThWepHMm671oB8imbpH1n0I58qhnCb9',
        'Origin': 'https://www.kuaicha365.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.kuaicha365.com/search-result?keyword=%E9%AA%8F%E6%90%8F%E4%BD%93%E8%82%B2%E5%8F%91%E5%B1%95%EF%BC%88%E6%B1%9F%E8%8B%8F%EF%BC%89%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&timestamp=1695573837574&source',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'hexin-v': hexin_v,
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'source': 'PC',
        'sw8': '1-YTBlNTJlMGItZDg2MC00YTQyLWFlNWYtZGQ4YmI1YmVjMzRi-YjYyMDdiYzAtZjZiNC00ZTg0LThiODktM2FmZTM0MzE5ZmRm-0-aXdjLXl1cWluZy1xZGMtcGMtZmUtcG9kPGJyb3dzZXI+-cGNfY2xpZW50XzEuNg==-dW5kZWZpbmVk-d3d3Lmt1YWljaGEzNjUuY29t',
    }
    json_data = {
        'page': 1,
        'page_size': 20,
        'keyword': keyword,
    }
    time.sleep(random.randint(1, 10))
    response = requests.post(
        'https://www.kuaicha365.com/enterprise_info_app/V1/search/company_search_pc',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()
    print(response)
