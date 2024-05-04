#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/10/17 21:17
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import hashlib
import json
import re
import time
import requests
class Tao_products(): #商品列表
    def __init__(self):
        with open('./package.json','r',encoding='utf-8')as f:
            data_json=json.load(f)
            self.url = data_json['products']['url']
            self.cookies=data_json['products']['cookies']
            self.cookie = data_json['products']['cookies']['_m_h5_tk'].split('_')[0]
            self.headers=data_json['products']['ALL_headers']
            self.queries=data_json['products']['queries']
            self.querie = data_json['products']['queries']['data']
        self.md5_s()
    def md5_s(self):
        da = int(time.time() * 1000)
        t_time= str(da)
        token = self.cookie
        d = token + "&" + t_time + "&" + '12574478' + "&" + self.querie
        md = hashlib.md5(d.encode())
        md5pwd = md.hexdigest()
        # print(md5pwd)
        self.re_sign(sign=md5pwd, t=t_time)
    def re_sign(self,sign=None,t=None):
        self.queries['sign']=sign
        self.queries['t']=t
        response=requests.get(url=self.url,params=self.queries,cookies=self.cookies,headers=self.headers)
        self.list_json(data=response)
    def list_json(self,data=None):
        json_s=data.text
        j=json_s.replace('mtopjsonp3',' ').replace('callback',' ').replace('(',' ').replace(')',' ')
        list_s=json.loads(j)
        resultList=list_s['data']['recommend']['resultList']
        for resu_list in resultList:
            creativeTitle= resu_list['creativeTitle']#工资名称
            itemId=resu_list['itemId']#id
            sellerNickName=resu_list['sellerNickName']#店铺名称
            provcity=resu_list['provcity']#店铺名称
            monthSellCountFuzzyString=resu_list['monthSellCountFuzzyString']#销售量
            url = resu_list['url']#详情页url
            promotionPrice=resu_list['promotionPrice']#价格
            print(creativeTitle,itemId,sellerNickName,provcity,promotionPrice,monthSellCountFuzzyString,url)




# if __name__ == '__main__':
#     Tao_products().md5_s()