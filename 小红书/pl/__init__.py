#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/10/12 22:53
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests
#url='device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7287818945891962153&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=117.0.0.0&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=150&webid=7287133158548440630&msToken=ZDjGJewnq_nrBRjiIrSCdHapLsmj32yUMzTPLVwet460Rgga0Oz9UMa9SsR5_QnMFI8VAO0EzqLcpsaz7NHvKifqdDveA7kp5BbDfMgACQ70Jn5uFww='
url='/api/redcaptcha/v2/getconfig'
data = {
    "group":"test_web",
    "action":"test_xb",
    "url":url
}
# header = {
#     'Referer': 'http://q.10jqka.com.cn/'
# }
res = requests.get("http://127.0.0.1:5612/business/invoke",params=data,)
d=res.json()
x_s=d['X-s']
cookies = {
    'a1': '1897da02d4b455unsq067nfelmvt4l1sc7p3xus1350000112133',
    'webId': '440f0cd1983884c8b68b46141f2c9b5c',
    'gid': 'yYjWf084jJSjyYjWf08JfW7M4D4227IMA8KWUyqIid16hq28941yMC888yyJyqq8id2j4yS2',
    'web_session': '030037a3889a8c3716fbb488c3234a091721b6',
    'abRequestId': '440f0cd1983884c8b68b46141f2c9b5c',
    'webBuild': '3.10.6',
    'unread': '{%22ub%22:%2264f87872000000001d016035%22%2C%22ue%22:%22650dd446000000001f004fe6%22%2C%22uc%22:22}',
    'xsecappid': 'xhs-pc-web',
    'acw_tc': '7bf4858da66343153f72db4c75235c5b8b65f54952c2c35395f93e38cb602f54',
    'websectiga': '7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4',
    'sec_poison_id': 'ce5a45d9-54a8-4c03-a32a-cc13bf0733f3',
}

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'a1=1897da02d4b455unsq067nfelmvt4l1sc7p3xus1350000112133; webId=440f0cd1983884c8b68b46141f2c9b5c; gid=yYjWf084jJSjyYjWf08JfW7M4D4227IMA8KWUyqIid16hq28941yMC888yyJyqq8id2j4yS2; web_session=030037a3889a8c3716fbb488c3234a091721b6; abRequestId=440f0cd1983884c8b68b46141f2c9b5c; webBuild=3.10.6; unread={%22ub%22:%2264f87872000000001d016035%22%2C%22ue%22:%22650dd446000000001f004fe6%22%2C%22uc%22:22}; xsecappid=xhs-pc-web; acw_tc=7bf4858da66343153f72db4c75235c5b8b65f54952c2c35395f93e38cb602f54; websectiga=7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4; sec_poison_id=ce5a45d9-54a8-4c03-a32a-cc13bf0733f3',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-b3-traceid': '6cd25fa00b085a56',
    'x-s': x_s,
    'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHAN0rIN0GjNsQh+aHCH0rhw/4DG/ZU8ezj+eLM4nEAq/Z9+9Ef8nlT4dcFJebAGA4IP7YMqArA+/ZIPeZlP/HlPAPjNsQh+jHCP/GE+ArUP0rUw/DIPaIj2eqjwjQGnp4K8gSt2fbg8oppPMkMank6yLELznSPcFkCGp4D4p8HJo4yLFD9anEd2rSk49S8nrQ7LM4zyLRka0zYarMFGF4+4BcUpfSQyg4kGAQVJfQVnfl0JDEIG0HFyLRkagYQyg4kGF4B+nQownYycFD9anksybSCy7kwPSkinp4zPDMongSw2DpE/LzyyLMTzfl+2DphnDzwySkLpgk+pbrU/gkd+LELc/p8PSQi/L4z+pSLc/pwJpLI/gk32DET//p8JLDMnSzQPLhUpfk8pFMCnS4ayDRop/zyyDExngkdPLMLLfTwPDLF/gknJpkong4ypFFMnSzwypkTLfY+pMkinpzBJbSxy74yzBPInp4b2DMga/bwzFFA/nMwyFMoL/+wzF8i/gkByLELLfkw2DkxnD4ByDEr8Ap8yfl3npziySkLpflwzBYT/D4BJpSxJBY8PSkx//QnyrMxnfMyprQk/nk8PSSLnfSwzFEx//QwyLELpg4+PSph/pzpPMkxnfSyzrkT/nMaJbSCag4OprSEnD4zPDhUag4wprrInfMtyrMoafkw2DExnSziJpkgz/b+zFpE//Q+PLExG7kOpbLA/fk0+rEg/fTyprEknSztyDMxn/bwzFDUnS482rRry7SyyDDI/nMpPpDUz/Q+JpQV/gkBJrMxp/QOprkV/MztybSL/g48pM8T/gkp4Mkxy74ypFFI/nM8PLET//+8pb8V/fknyLhUaflwySQ3nfk02rMCafTwzMrA/DzDyrMrp/bOzFkV/pzd2rFU/gSwySb7/gkm4FRon/myzrkk/D4b4MkxJBlwzFLMnp4b4FMoLgYycFiEHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/cDMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRAyfRL+gSl4bYlqg48qDQlJFShtUTozBD6qM8FyFShPo+h4g4U+obFyLS3qd4QyaRAy9+0PFSe/B8QPFRSPopFJeHIzbkA/epSzb+t8nkn4AmQynpS2b87/sTc4BRUqgzit7i78nTTpAzQ2sTkanYULdkn494NLoz8a/+zLBRra9L9qgziagW6qA8n4BRQyLM6anSi8n4s+fp/8omiqf89q9kM4rTUnf4S8f+Uwn4fa9p8GMmSagYS8LzM4B+QznpS8SmFcnR8appF8rl1agWMqA+l4bQ1GA4Spf8otFS3G74QyLYF+emj/LS9yobFLAYdanSk8dmn4FbQcFYnafuA8p+I8np3LoznagWA8/mxaeFjNsQhwaHCN/DM+0L7+/rh+UIj2erIH0il+/8R',
    'x-t': '1697122129901',
}

response = requests.get(
    'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id=6511c29c000000001e02959b&cursor=&top_comment_id=&image_scenes=FD_WM_WEBP,CRD_WM_WEBP',
    cookies=cookies,
    headers=headers,
).json()
print(response)
