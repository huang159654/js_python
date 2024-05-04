#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/4/9 16:37
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re
import urllib.parse

import execjs
import requests

cookies = {
    '_m_h5_tk': 'de4b18b33ec6e38668dbcdf8270c0943_1712937465318',
    '_m_h5_tk_enc': '469c5ddfb543dd548679ea60b876d07f',
    'tfstk': 'fjCmn6qjntJb220Tm_AbZAcOilyRLnOe_nS9XhQwbExW01UXXCVGV3LqQflNEhjPqn-Y5PGMQ38K3j8q_48yRFk27n7ZSFSR4Gv_lhKwjGQNHzFL9Z_X1CSgvWFLynF_4iY23d8z7F8idbmTuZ_X14g-bJBPlAvvuK12_GRyze89_jk20zvyJFRZgdlVz3-W7C-NbhRPzeYD7Elw04lmgf-h__1zRjWNliAmQVLMnH7udflgEEopxZ-o_fJ9oK0Ru3cZ__XWsvh20JgJfIKfrEj_OjO2IO5vasrz_BWCq1vetRUX3NXlfICz7x-FHidPg90Z_aADbMCyUmqkYs_POQJ8TybPNiQfZN3a_UIp4Z12sWzBiI-2ZU1TVj-GUO5vhCi4jh1lzsWG4jHrL1Wm1UzOaAM63UTkA6VoGnWYQfJ0rzDQhK8WkkUurAik3UTkjz4odqJ2PEEd.',
    'isg': 'BDEwU7_g89mHD1_ceXrb-HwaQL3LHqWQt1qhYxNG_fgXOlCMW2rRYMAYXM5cyT3I',
}



headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'JSESSIONID=086A59471066F976D5FC372679E40694; _m_h5_tk=ac8098a192262210ec7e158f5a7b03c3_1712848964590; _m_h5_tk_enc=22f761f01cbd91cee72d469670dacb66; tfstk=flmKnOcpQCAnhrYoAvTizmrzPPpihEfEL5GCqgqutFGT1jghqeuHeVeun_1SFBl-25GZr4vUrfQ_n87CNgN7CAw0EMaSq7mJekoi-gVHTuHSiudDinxmLvrUVIAcmyraNow8d8_CZGa1kU-o8nxmLv63dKD6mL5hdcPzNuaQNNt__-s7Nba5fANaU81QVW9tC5y7V8Z5VP1_nJwQNgGDFQF1d7j-b3wLvBCAb-yrXJU6SvNssXvudyFjd5dJwcCzJSMQ6gOm-tSbw5oXsFHZN2G3QbKv6ogq60Ub2HC4pVMYfWqXkNEKIXoYAmddxR489ViQWTsShvPTk4hp9wPI-fU4CP6J0Rc01voIWL5sdjVLARaMcKH_PVmUuDA1vogqKk0SGCb3Oqe54DimDpodiSelRdpOzazQIiCikUjySfIgBSvp2a7z7dyTidpVzazQdRFDpCbPzPJN.; isg=BM3MKgBal7sMwjOIhY4_RLhG3OlHqgF8cxaNlw9QJ2TTBuy41_54TC_UcJpgwxk0',
    'pragma': 'no-cache',
    'referer': 'https://detail.1688.com/offer/653588440523.html?spm=a260k.24512198.kt9jg2cz.1.7c1a5440QVwIn2',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

params = {
    'spm': 'a260k.24512198.kt9jg2cz.1.7c1a5440QVwIn2',
}

response = requests.get('https://detail.1688.com/offer/653588440523.html', params=params, cookies=cookies, headers=headers)
p_t=re.findall('\"t\"\:\"(.*?)"',response.text)[0]
x5secdata_s = re.findall('\"SECDATA\"\: \"(.*?)"\,', response.text)[0]
slidedata_t = re.findall('\"NCTOKENSTR\"\: \"(.*?)"\,', response.text)[0]
n = execjs.compile(open('f.js', mode='r', encoding='utf-8').read()).call('get_url',slidedata_t,x5secdata_s)
print(n)
# dsas = 'https://detail.1688.com/offer/page/detail.htm/_____tmd_____/slide?slidedata=' + keywords
# print(dsas)
# dsg='https://detail.1688.com/offer/page/detail.htm/_____tmd_____/slide?slidedata=%7B%22a%22%3A%22X82Y__0e1748d45e9398849fd9ba9e6eb0c705%22%2C%22t%22%3A%2222448252081daf22eef4b292361e934e%22%2C%22n%22%3A%22227!SSiSphVK3GfYF1mBNU9g5DudZ%2BP4JL9j4lPPOrzYq%2FXWntR3SCcTpsrUVgiE9O3aPEMwCSPE8mJMtS3Oe8xcJPWY6%2Bo1wHRenHEueEjypCASntkk%2BVnL3SIb%2B%2BTfrYvq%2Bl7ersvHQaScFomTAnIlahZkFLNXmpYinHEVOmv3ehuoz98uckn13DmWqAgHmppinHPkqfvHaRbgh70Ke8lnODlzqKiHDppinXPPOfHhm9mHtdR8mxnD3Xlz1QVXiZce%2BSVuO9ojaCKHnWB8rxvG3DQHqXRKSZcFSDE4OJvHaEJzHtkiRxjl3lQHqDdXYZWBHXE4OKMQaRKpHokAmxnL3rqzqQrGrRSinGypODjX5CSS6dR8l86D3SS1qKCXDpvCnHEuO2nXaR3SsbEplv%2BR3DQWqm5ncZvCnHEu%2FaZCGKyxgV3tJR6vCQo6eSzzl1CKOkfYy8WNzAyRgfZtJLXl5QyigJ%2F4cnuBE4jzy8vU9ZgsNaR%2FoljH%2BcNbMhWURIjI2ZdVlXRqT2y9u2tU%2Ff2Jn28sg2SfJ0IE9VoazRw3qQIRE5HZTMJm0AWajU1wSZLmvdo1NtJV67Pcq6N6B9sZQJ0JRaztAzQtkvPrw%2FD9gz%2Fcrz58kRe0u8RObJoUv7F0rKr7MPb85ARRYjzVwfLAc1UIAu0wlcKoQb5acp5lw9tHHNgvGOnUjmoEKW%2BYGtwVCVNUxbRqlnd1qXgQxOyiUETO5ggH%2FB%2BhBsrfNSieKRyrrkXuNAYptJpI%2BAT%2BeWWkus0OD6zsk2i%2BqxjcG5lo10Edk5N1jBG61vK8u%2Bm1%2FvSEQmXsM6hkDNV%2FSse7QiXc4GcBDkoCIE3UcqrYdtszHEPJ7J4sMiknQoaLjLQnk1k%2BsRfWqwf%2FlVixt0gT6mTvuRZruR0pMvSSLegwf%2BbjFHHM8VoYCGh8GTWnD3rgPkW2LKLxhg%2FuMAmxYQkoEn9hClb0aOVkzRckjwHDejcwbnjViGaIgml5lPZOduYARALV9O4ihfKq%2BKFvbcS6HGtcw9a8pfoFheV81nDli0LLWr98te5l6%2B2m8fkObZGrLoDJfeLqAE2zrZ7623z7i6s7Z1wcNlJl01jOz5IFcf2hapsak%2FqnxT14%2BdKd%2B3VqAE5kSS7grz0J%2FDUwVcvNuUaE%2ByVoskNNn9LHV4%2F%2FKMkqMGhMiFoRvbm64y23Z6UnfkoKWqwlOm7rTkWw6HPA79c4%2BQg2ubDkOl646Bm8ZDqctSgms3anQjrnfsoVl%2BgI6hbkCDzdP8mh1CcENR2wJ8drDwoM53lV2KVVhh7Wzrhc6%2FgCxtMC89LfKENp%2FK6T1w7W8Ns%2FNTXimM6i6OFaReUEeg%2B6fqVqFb%2FhZIpjYjl1QGIACpATPi4EzfipfEVu927iaNmFIFNfpqMbmfDPyAeZinVShXb5LRQDMstt6tIcHG7dku%2B0ZXXtOXOWjsnlgehbRBGMElF15MVJYQA7M5Zo2caax3XdefBnZ%2B%2FnaR5WzZdQAftlmAOfK4PduwexKYY5EFdDhQjnnBaOEIQqdecF1ahCmYu%2BmCHE5WBv%2Fxme2%2BPLniFaOJgI9yWKUOpbEQ7%2ByQNI03BibHgg8zdf2KRXi3%2FYVK91DEXFW6rZmbjsgdMWVdExu%2Fmri3JI21HUBn4Mk%2BCyyoHRdaDaeikbISgSkqceFtbtTVD70f7YT1unFvFq8ixYlgU87pVjbUpnTPYlC4DSe0MLm0rK%2FXDeYkS9h559o7x6h7jXEQT4WvzgpxePBmpV21SwTEsn4EF196bG%2Bu9YlMCDVDaH5lt74BE4%2FbLIJvDNPq7ovLvfFqezUoTKfi%3D%3D%22%2C%22p%22%3A%22%7B%5C%22ncbtn%5C%22%3A%5C%22795.5%7C268%7C42%7C30%7C268%7C298%7C795.5%7C837.5%5C%22%2C%5C%22umidToken%5C%22%3A%5C%22G6A726EE90103356D1DF744C98407D490718A61A44686AC3552%5C%22%2C%5C%22ncSessionID%5C%22%3A%5C%225e701f13f8ef%5C%22%2C%5C%22et%5C%22%3A%5C%221%5C%22%7D%22%2C%22scene%22%3A%22register%22%2C%22asyn%22%3A0%2C%22lang%22%3A%22cn%22%2C%22v%22%3A1%7D&x5secdata=xd33ee7ec46d9a197e22448252081daf22eef4b292361e934e1712928849a-1109984729a88757878abazc2aaa__bx__detail.1688.com%253A443%252Foffer%252Fpage%252Fdetail.htm&ppt=3&landscape=1&ts=1712928919880&v=03382454890789004'
# print(dsg)
# url='https://detail.1688.com/offer/page/detail.htm/_____tmd_____/slide?slidedata=%7B%22a%22%3A%22X82Y__0e1748d45e9398849fd9ba9e6eb0c705%22%2C%22t%22%3A%2291651a857b3db345a37c9b9fe8487eea%22%2C%22n%22%3A%22227!SSiSphiPBnX42Bcuci3HtDudZ%2BP4JL9j4lPPOrzYq%2FXWntR3SCcTpsrUVgiE9O3aPEMwCSPE8mJMtS3Oe8xcJPWY6%2Bo1wHRenHEueEjypCASntkk%2BVnL3SIb%2B%2BTfrYvfdl7ersvHQaScFoojAnIltSI2F2AXmpYinHEVOmv3ehuoz98uckn13DmWqQgHmppinHPkqfvHaRbgh70Ke8lnODlzqKiHDppinXPPOfHhVLulUoR8mxnD3XlzsQVXmpwa%2B6ElOyQ7a7mWjtRhSfnLfiaWqK%2BSmppinXPPOJjXa7mHntkhY2nffCsAqKCXDpABEDPPOJjXUxSiuKyxgV3tJhe8Cm%2Fd7SzcRIRx%2Fkfiy8WNWA9hgfZtJLXN5QyC1sODg%2F2PRffCL3dcSVScDJxHXh%2FTzT1Lp1GlGewSnfyjMKAKq0eBtJrn5ggdDiuQm7nye2T23Keyx9k5QnZi%2FKtUDe%2BMRxeS6ZKFYrNEzqAVqGNm4Es2c%2FwUuV%2FDhkvx5Vf3oTpAmB%2BLnzEN%2FLEi9kket6n82VPzDUb5GEs1hzzOb7nY5V%2BNwvFIfapA%2F87GlIRb%2B9HdoBC2zSP2svT3Y14b2jW3hYRFXklzGDumiur6VzBQ84hPe2AAdn8bBkfol%2BKcWXVuYy13OOScMS2j2qNZbDJUVrN69mixpvHzLrh4fVyeOo%2BxJJT9pkjDHvIxhNNv3f5KsSD3hsVL%2FY%2BMkE8hgLuD%2Fvxru4nM7HKV15Nkj1GVIt1PEHihuC6iLwQXBq%2FIf%2Fds70n1SBWN76yjXBfl46BPZsXBJwJK2qajxRNMiqEcH3WoBLUQVWVy86mf90UwwMd%2BYsUDwBhBZfx2frZ5aOyuSigcLbN%2BnIvq7RgRbDS5zcrje8%2Bwmbphsw95Pke44ti1JNduAa5rXgqfBaBax%2BNFWoWO3%2FV2NHbfsJB8qY5by54pjEfmFTbjCNiiVKdihx4XMPCoAp20VQELuRncycMrk8M%2Bn%2FiKM4blOlxL2Vnko7mfFmSTsik04lllJj2c%2FF5PCrTYkegiHSznRvpc3W4JaLX1%2BDDpPruVcAHpdPM56wEuyDDzJsL6UfB8ZxnIGtgTBcv5p9edBphzb9uAsrPzdxSpJnJsNDN5zSZR1UkT2ZsCkHHWT7IjQIUJ1l158ZlrKgVSq2TPWvUd8nJmCzldNgj%2FX%2BhVhnpVkHXXF9obWqohySr1%2FVcAemXmUy%2F%2B4pIYyiA%2BuAA5DAfqyq7sOmxeyaf1YzvCoL%2FohB%2FWYrFO26JOkA6bRQ14JQxINLqEW0PHBSMsiFS4JssE6a2keJYjR5AtQCWxYmf1tfMOHfY5xXnbw0OyqDw0D1bBxgq%2BF1bnRKCHY0brr0tnibd89S7tNq7RE4U%2BXs8p%2FZBG0c3La%2FBTTvUJiQ9%2FYrQ77X5WcT52IMNuK5V28YPj6lgbwn4pWLopcpJBsh%3D%3D%22%2C%22p%22%3A%22%7B%5C%22ncbtn%5C%22%3A%5C%22795.5%7C263.5%7C42%7C30%7C263.5%7C293.5%7C795.5%7C837.5%5C%22%2C%5C%22umidToken%5C%22%3A%5C%22G75FC3D331113E6E27B062AE23F1D434237D839602D1AA05250%5C%22%2C%5C%22ncSessionID%5C%22%3A%5C%225e701f13f8d8%5C%22%2C%5C%22et%5C%22%3A%5C%221%5C%22%7D%22%2C%22scene%22%3A%22register%22%2C%22asyn%22%3A0%2C%22lang%22%3A%22cn%22%2C%22v%22%3A1%7D&x5secdata=xd4637549ff7c1a4a391651a857b3db345a37c9b9fe8487eea1713070839a-1109984729a88757878abazc2aaa__bx__detail.1688.com%253A443%252Foffer%252Fpage%252Fdetail.htm&ppt=3&landscape=1&ts=1713070843921&v=06179542475967423'
res = requests.get(n,headers=headers,cookies=cookies)
print(res.json())