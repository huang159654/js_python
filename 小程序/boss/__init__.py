#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/10/19 22:03
# @Author  : TS
# @Email: TS@gmail.com
# @File : ts2.py
# @Software: PyCharm
"""
import requests
url='https://www.zhipin.com/wapi/zpgeek/miniapp/homepage/recjoblist.json?cityCode=101230500&sortType=1&page=1&pageSize=15&districtCode=&mixExpectType=1&expectId=-1&blueWelfare=&appId=10002 HTTP/1.1'
headers = {
 'Host': 'www.zhipin.com',
 'Connection': 'keep-alive',
 'wt2': 'D6OkbU2R6ng1TNrHUg83A_Hogy-Lrz-8zRz345RG3DsaAKBE4U0yAm49a31PRnDU3lOCh2BmnPMqYMYTOMa2C3w~~',
 'zpAppId': '10002',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
 'Content-Type': 'application/x-www-form-urlencoded',
 'mpt': '75a5c1c529feab31a0dcf07a934c15c6',
 'scene': '1053',
 'xweb_xhr': '1',
 'x-requested-with': 'XMLHttpRequest',
 'miniappVersion': '5.2000',
 'platform': 'zhipin/windows',
 'ver': '5.2000',
 'Accept': '*/*',
 'Sec-Fetch-Site': 'cross-site',
 'Sec-Fetch-Mode': 'cors',
 'Sec-Fetch-Dest': 'empty',
 'Referer': 'https://servicewechat.com/wxa8da525af05281f3/470/page-frame.html',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept-Language': 'zh-CN,zh;q=0.9',
}
res=requests.get(url=url,headers=headers)
print(res.json())