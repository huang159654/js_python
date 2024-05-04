import json

import execjs
import requests

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1684909695',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1684939524',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1684909695; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1684939524',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLVOBvRPUTl5FDTuar3rUWIuhpUUKvcMtoMqfGfwdLCb8g==',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}
for pg in range(0,31):
    params = {
        'pg': '0',
        'pgsz': '15',
        'total': '450',
    }
    response = requests.get(
        'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
        params=params,
        cookies=cookies,
        headers=headers,
    ).text
    json_data=execjs.compile(open('./data.js','r',encoding='utf-8').read()).call('h',response)
    # print(json_data)
    json_list =json.loads(json_data)
    dict_data=json_list.get('data').get('list')
    for ID in dict_data:
        dict_ID = ID.get('QY_ID')
        params_1 = {
            'compId': dict_ID,
        }
        response = requests.get('https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/compDetail',
                                params=params_1, cookies=cookies, headers=headers).text
        # print(response)
        json_data_1 = execjs.compile(open('./data.js', 'r', encoding='utf-8').read()).call('h', response)
        json_sa = json.loads(json_data_1)
        json_QY_NAME = json_sa.get('data').get('compMap').get('QY_NAME')  # 公司名称
        json_QY_ORG_CODE = json_sa.get('data').get('compMap').get('QY_ORG_CODE')  # 统一社会信用代码
        json_QY_GSZCLX_NAME = json_sa.get('data').get('compMap').get('QY_GSZCLX_NAME')  # 企业登记注册类型
        json_QY_REGION_NAME = json_sa.get('data').get('compMap').get('QY_REGION_NAME')  # 企业注册属地
        json_QY_FR_NAME = json_sa.get('data').get('compMap').get('QY_FR_NAME')  # 法定代表人
        json_QY_ADDR = json_sa.get('data').get('compMap').get('QY_ADDR')  # 企业经营地址
        params_2 = {
            'qyId': dict_ID,
            'pg': '0',
            'pgsz': '15',
        }

        response = requests.get(
            'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/caDetailList',
            params=params_2,
            cookies=cookies,
            headers=headers,
        ).text
        json_data_2 = execjs.compile(open('./data.js', 'r', encoding='utf-8').read()).call('h', response)
        json_sa_2 = json.loads(json_data_2)
        list_data = json_sa_2['data']['pageList']['list']
        params_3 = {
            'qy_id': '002105291239451309',
            'projectType': '01',
            'pg': '0',
            'pgsz': '15',
        }

        response = requests.get(
            'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/compPerformanceListSys',
            params=params_3,
            cookies=cookies,
            headers=headers,
        ).text
        json_data = execjs.compile(open('./data.js', 'r', encoding='utf-8').read()).call('h', response)
        json_sa_4 = json.loads(json_data)
        data_list = json_sa_4.get('data').get('list')
        list_data_da = []  # 工程项目
        for data in data_list:
            data_PRJNAME = data.get('PRJNAME')
            list_data_da.append(data_PRJNAME)
        list_data_1 = []  # 企业资质资格
        for i in list_data:
            i_APT_NAME = i.get('APT_NAME')
            list_data_1.append(i_APT_NAME)
        print(json_QY_NAME,
              json_QY_ORG_CODE,
              json_QY_GSZCLX_NAME,
              json_QY_REGION_NAME,
              json_QY_FR_NAME,
              json_QY_ADDR, list_data_1, list_data_da)
