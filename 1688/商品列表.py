#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/10/15 23:22
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import hashlib
import json

import requests


class A_1688():
    def __init__(self):
        with open('./package.json','r',encoding='utf-8')as f:
            list_data=json.load(f)
            self.cookies=list_data['cookies']
            self.cookie = list_data['cookies']['_m_h5_tk'].split('_')[0]
            self.headers = list_data['ALL_headers']
            self.url = list_data['url']
            self.params = list_data['queries']
        self.sign_s()
    def sign_s(self):
        token=self.cookie
        #keywords 手动替换 brandPid手动替换
        data='{"keywords": "运动户外","brandPid":"220127_0001","appName":"brandPcRender"}'
        d = token+ "&" + '1697463126836' + "&" + '12574478' + "&" + data
        md = hashlib.md5(d.encode())
        md5pwd = md.hexdigest()
        self.response_s(data=md5pwd)
    def response_s(self,data=None):
        keywords = input('请输入搜索商品名字:')
        self.params['sign'] = data
        self.params['keywords']=keywords
        list_data=requests.get(url=self.url,params=self.params,headers=self.headers,cookies=self.cookies).json()
        self.lidt_json(data=list_data)
    def lidt_json(self,data=None):
        offerResult=data['data']['content']['offerResult']
        for eurl in offerResult:
            eurl=eurl['eurl'] #详情页
            strPriceMoney=eurl['strPriceMoney']#价格
            title=eurl['title']#名称
            print(eurl)




if __name__=='__main__':
    A_1688().lidt_json()