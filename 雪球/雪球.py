import re

import requests

cookies = {
    'cookie2': '15187275d9931d6d602bca3b15ae39a7',
    't': '10fd35ea3b6c764eaf236f85e5e710fd',
    '_tb_token_': 'e53771eebba4b',
    'lid': 'tb8575830936',
    'cna': 'UvgmHQGEvV0CAXAv8H7srl+q',
    'xlly_s': '1',
    '_bl_uid': '4plgatw7qFbxsqe6syUym24t2ev1',
    'ali_ab': '2409:8a50:c431:fc0:2051:ee4b:dadb:a98b.1710405911143.1',
    'sgcookie': 'E100yjnDIp4HdfyGdOqIOaPUBB4pHt8dQYFtrKQmMrIBSel2iUWSjgdY0mQgTwAwVqS9RS9fOG%2BCQAVgd3Wkuz00Vtw%2B55DPk7K7yvrB%2BYUqO72qwvl4tlBCgiSTIsnPbUK1',
    'csg': '481e60d4',
    'uc4': 'nk4=0%40FY4Gtw7VYB9A1XG6%2BKBBI8Cn3MaJTGE%3D&id4=0%40U2grGNttG3Y0yNQxNjlY%2F7xHUkf3TdFQ',
    '__cn_logon__': 'true',
    '__cn_logon_id__': 'tb8575830936',
    'ali_apache_track': 'c_mid=b2b-2209129856502c7293|c_lid=tb8575830936|c_ms=1',
    'ali_apache_tracktmp': 'c_w_signed=Y',
    '_csrf_token': '1710406723358',
    '__mwb_logon_id__': 'tb8575830936',
    'mwb': 'ng',
    '_m_h5_c': '2ff8ae98d5d5d54bdfee9bdbe8d2e24a_1710498830304%3Bc10f670f059dea069347c25f6914ca3f',
    'taklid': 'aca1158a4abd47c78af130c81cb13634',
    'keywordsHistory': 'usb-c%3Bc%3B%E8%BF%90%E5%8A%A8%E6%88%B7%E5%A4%96%3Busb-cx%3Bsb-cx%3B%E6%BA%9C%E5%86%B0%E9%9E%8B',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': 'a34f052b69d0679ca6976c0c17572b28_1710520205323',
    '_m_h5_tk_enc': '7b56b48309df454fecfe4a503234a579',
    'tfstk': 'fDcq1uVcYId4uk-fdoPaLFqsKkNYIWKImfZ_SV0gloq0cKLN_uzNIGfiSloZVuH6knEsbR0b2jTYChHP72nz1cu9kPqijcrshLOIkqFTsHiwOBgYzJgyvjPGf4VCU3fHABOIoK4Y14xBkks5rJzgsrqci7Yzky60s-4GZUzg5iXGic0kkYiRnNW_hH0LqbNuudCXemEPs17Lu-qH9u5Gsbzqzk0DJ1fiaryq_IOBMQwjI2eKGDRNwSgEE74Z6eXabJkiG7cDqB28IbmurmT1BzkZSXFYTNAmzSr4KfoR-6onzVDQUbTH9SP0mANx5w-jzjojkbu1STV4GYyEgWjPnGUoYfct3GXanzUzAU8PwCjxuBURBtWOB8VLzkTblOBTnzazAU8PBOeuAzrBlr1..',
    'isg': 'BE5ODErZp00DOxO2V4ib01cfnyQQzxLJyLw163iXrNEM2-814Fh02QuZFwe3Qwrh',
}

headers = {
    'authority': 'sale.1688_.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'cookie2=15187275d9931d6d602bca3b15ae39a7; t=10fd35ea3b6c764eaf236f85e5e710fd; _tb_token_=e53771eebba4b; lid=tb8575830936; cna=UvgmHQGEvV0CAXAv8H7srl+q; xlly_s=1; _bl_uid=4plgatw7qFbxsqe6syUym24t2ev1; ali_ab=2409:8a50:c431:fc0:2051:ee4b:dadb:a98b.1710405911143.1; sgcookie=E100yjnDIp4HdfyGdOqIOaPUBB4pHt8dQYFtrKQmMrIBSel2iUWSjgdY0mQgTwAwVqS9RS9fOG%2BCQAVgd3Wkuz00Vtw%2B55DPk7K7yvrB%2BYUqO72qwvl4tlBCgiSTIsnPbUK1; csg=481e60d4; uc4=nk4=0%40FY4Gtw7VYB9A1XG6%2BKBBI8Cn3MaJTGE%3D&id4=0%40U2grGNttG3Y0yNQxNjlY%2F7xHUkf3TdFQ; __cn_logon__=true; __cn_logon_id__=tb8575830936; ali_apache_track=c_mid=b2b-2209129856502c7293|c_lid=tb8575830936|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; _csrf_token=1710406723358; __mwb_logon_id__=tb8575830936; mwb=ng; _m_h5_c=2ff8ae98d5d5d54bdfee9bdbe8d2e24a_1710498830304%3Bc10f670f059dea069347c25f6914ca3f; taklid=aca1158a4abd47c78af130c81cb13634; keywordsHistory=usb-c%3Bc%3B%E8%BF%90%E5%8A%A8%E6%88%B7%E5%A4%96%3Busb-cx%3Bsb-cx%3B%E6%BA%9C%E5%86%B0%E9%9E%8B; mtop_partitioned_detect=1; _m_h5_tk=a34f052b69d0679ca6976c0c17572b28_1710520205323; _m_h5_tk_enc=7b56b48309df454fecfe4a503234a579; tfstk=fDcq1uVcYId4uk-fdoPaLFqsKkNYIWKImfZ_SV0gloq0cKLN_uzNIGfiSloZVuH6knEsbR0b2jTYChHP72nz1cu9kPqijcrshLOIkqFTsHiwOBgYzJgyvjPGf4VCU3fHABOIoK4Y14xBkks5rJzgsrqci7Yzky60s-4GZUzg5iXGic0kkYiRnNW_hH0LqbNuudCXemEPs17Lu-qH9u5Gsbzqzk0DJ1fiaryq_IOBMQwjI2eKGDRNwSgEE74Z6eXabJkiG7cDqB28IbmurmT1BzkZSXFYTNAmzSr4KfoR-6onzVDQUbTH9SP0mANx5w-jzjojkbu1STV4GYyEgWjPnGUoYfct3GXanzUzAU8PwCjxuBURBtWOB8VLzkTblOBTnzazAU8PBOeuAzrBlr1..; isg=BE5ODErZp00DOxO2V4ib01cfnyQQzxLJyLw163iXrNEM2-814Fh02QuZFwe3Qwrh',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'memberId': 'b2b-22141608879079c699',
    'aHdkaW5n_isCentral': 'true',
    'aHdkaW5n_isGrayed': 'false',
    'aHdkaW5n_isUseGray': 'true',
}

response = requests.get('https://sale.1688.com/factory/card.html', params=params, cookies=cookies, headers=headers).text
dsd=re.sub(r'\s+','',response)
print(dsd)