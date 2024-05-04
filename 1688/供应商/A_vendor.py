#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/21 16:44
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import re

import requests


class AL_vendor():
    def __init__(self):
        with open('./package.json','r',encoding='utf-8')as f:
            json_data=json.load(f)
            self.url=json_data['vendor']['url']
            self.headers = json_data['vendor']['ALL_headers']
            self.cookies = json_data['vendor']['cookies']
    def AL_requests(self):
        headers=self.headers
        cookies=self.cookies
        url=self.url
        response =requests.get(url=url,headers=headers,cookies=cookies).json()
        return response
    def AL_response(self):
        data=self.AL_requests()
        self.AL_parse(data=data)
    def AL_parse(self,data=None):
        if data['data']['data']['companyWithOfferLists']:
            for companyModel in data['data']['data']['companyWithOfferLists']:
                domainUri=companyModel['companyModel']['domainUri'].split('.')[0]
                # print(domainUri)



class AL_Contact():
    def __init__(self):
        with open('./package.json','r',encoding='utf-8')as f:
            json_data=json.load(f)
            self.url=json_data['Contact']['url']
            self.cookies = json_data['Contact']['cookies']
            self.headers = json_data['Contact']['ALL_headers']
            self.queries = json_data['Contact']['queries']
    def AL_responses(self,):
        data=AL_vendor().AL_response()
        print(data)
        # self.AL_data_assembl(data=data)
    def AL_data_assembl(self,data=None):
        pass
        # print(data)
        # queries_data=self.queries['data']
        # print(queries_data)
        # data_params=re.sub('kejia365','shop76217l90s7406',queries_data)
        # print(data_params)
    def AL_Crequests(self):
        url = self.url
        cookies = self.cookies
        headers = self.headers
        queries = self.queries
        response=requests.get(url=url,params=queries,headers=headers,cookies=cookies)
        return response
    def AL_Crespons(self):
        data=self.AL_Crequests().text.replace('callback(','').replace(')','')
        json_data=json.loads(data)
        self.AL_Cparse(data=json_data)
    def AL_Cparse(self,data=None):
        if data['data']:
            mobileNo=data['data']['mobileNo']#手机号
            companyName=data['data']['companyName']#公司名称
            print(mobileNo,companyName)



if __name__=='__main__':
    # AL_vendor().AL_response()
    AL_Contact().AL_responses()