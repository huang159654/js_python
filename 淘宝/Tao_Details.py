#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/23 15:57
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import hashlib
import json
import time
import urllib.parse

import requests


class Tao_Details():#商品详情页
    def __init__(self):
        with open('./package.json','r',encoding='utf-8')as f:
            data_json=json.load(f)
            self.url=data_json['product']['url']
            self.cookies = data_json['product']['cookies']
            self.headers = data_json['product']['ALL_headers']
            self.queries = data_json['product']['queries']
            self.cookie = data_json['product']['cookies']['_m_h5_tk'].split('_')[0]
            self.querie = data_json['product']['queries']['data']
    def def_Tid(self):
        pass
    def def_Tsign(self):
        da = int(time.time() * 1000)
        t_time = da
        token = self.cookie
        d = token + "&" + str(t_time) + "&" + '12574478' + "&" + self.querie
        md = hashlib.md5(d.encode())
        md5pwd = md.hexdigest()
        self.def_Trequests(sign=md5pwd, t=t_time)
    def def_Trequests(self,sign=None,t=None):
        self.queries['sign']=sign
        self.queries['t']=t
        response=requests.get(url=self.url,params=self.queries,cookies=self.cookies,headers=self.headers)
        print(response.text)
        # self.def_Tresponse(data=response)

    def def_Tresponse(self,data=None):
        pass
        json_s = data.text
        j = json_s.replace('mtopjsonp2', ' ').replace('callback', ' ').replace('(', ' ').replace(')', ' ')
        list_s = json.loads(j)
        print(list_s)
    def def_Tcsvs(self):
        pass
if __name__=='__main__':
    Tao_Details().def_Tsign()