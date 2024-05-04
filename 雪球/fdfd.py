#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/4/12 14:26
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests

cookies = {
    'arms_uid': 'd4cf8c8a-d825-4b4c-b235-4713cfe9ee0d',
    'cookie2': '17f2ec7deac2eb3a95d7b02fe7590b17',
    'mtop_partitioned_detect': '1',
    'cna': 'NsKfHuuJ9X4BASQJilBlVny5',
    'xlly_s': '1',
    'tfstk': 'enRyqt1ubbhyWha6UtfFQZh_qI1Rt1n1qBsC-eYhPgjov4QhT3tcKab3trv2xnB5q_gLLW8FDJ2lqa40oNQGx8XhqKzeWn5BYe3R-MxHYM9ShfTJy6CnfHls1UKVtlpEfNIq-SCdtci_hWX-_6K_Y-CFYQxmdrnG3cYOmIMvg6OgKHI4t5zOzTm2zJNUTI7PUUL50t6XgaWPjgoQvZxwtBpzxJWlkZSsuqyR2y4kAaHkVJedn1QVf4_7pJBl7ZSsu4wLptjluGg5P',
    'isg': 'BEhIJA7zunPrVdbnSGUCY509GbZa8az7dp1ouAL5HkO03elHqgJKixWbVbWtVmTT',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-pp': '78613a34653938393964663536626132326335623032633261326230393962313066623a307c307c617c313731323930333433363239327c6d64357c7177656173647a7863677c317c317c7c78726a704a487350547759446b736c507c303a78726a704a487350547759446b736c503a303a3336326236326565383338623532306639386432353466323861653239323962626161653465313061333161653836623132643433333939306538633564353636353434666234373639356166393039643037333430363939383563623730623a30',
    'bx_et': 'eDdHq6mQKpWChsFXWHCIs8mxTyMOdk15f3FR2_IrQGS6wpI-db0lja2z478Pq3xOfMp-P26yjZb0TJPzaN7NPZbzTURRzQx1TT9d2MIlZUtmWmhxMeTCN6oxDjCFAyfca-Ng228BR_1zWukvQewld-jlYL24FUE6t2XAmrUaay6zn_I28M8pJCuPLJThjvMpsnBC0mIga7RG-go_Q-RyK7_ZyCy7F971SidmsWseGgBU3V0ghv6F5wnxSV27j971Sg0iS-aFLN_KD',
    'cache-control': 'no-cache',
    # 'cookie': 'arms_uid=d4cf8c8a-d825-4b4c-b235-4713cfe9ee0d; cookie2=17f2ec7deac2eb3a95d7b02fe7590b17; mtop_partitioned_detect=1; _m_h5_tk=361fac03a7abdad91a651c60c501e221_1712912434985; _m_h5_tk_enc=34f57f2c224c3cd939d3993956648b05; _m_h5_tk=ffe57a2252c5db96eb6ea4355c59dd08_1712912795176; _m_h5_tk_enc=1873e4fb3ec2e7ba65496db5a6377ee4; cna=NsKfHuuJ9X4BASQJilBlVny5; xlly_s=1; tfstk=enRyqt1ubbhyWha6UtfFQZh_qI1Rt1n1qBsC-eYhPgjov4QhT3tcKab3trv2xnB5q_gLLW8FDJ2lqa40oNQGx8XhqKzeWn5BYe3R-MxHYM9ShfTJy6CnfHls1UKVtlpEfNIq-SCdtci_hWX-_6K_Y-CFYQxmdrnG3cYOmIMvg6OgKHI4t5zOzTm2zJNUTI7PUUL50t6XgaWPjgoQvZxwtBpzxJWlkZSsuqyR2y4kAaHkVJedn1QVf4_7pJBl7ZSsu4wLptjluGg5P; isg=BEhIJA7zunPrVdbnSGUCY509GbZa8az7dp1ouAL5HkO03elHqgJKixWbVbWtVmTT',
    'pragma': 'no-cache',
    'referer': 'https://detail.1688.com/offer/653588440523.html?spm=a260k.24512198.kt9jg2cz.1.7c1a5440QVwIn2',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://detail.1688.com/offer/page/detail.htm/_____tmd_____/slide?slidedata=%7B%22a%22%3A%22X82Y__0e1748d45e9398849fd9ba9e6eb0c705%22%2C%22t%22%3A%22546fdebaca1dec6ae16cd92dd71b2b1d%22%2C%22n%22%3A%22227!SSiSphiLGiciVYn3ci3HhDudZ%2BP4JL9j4lPPOrzYq%2FXWntR3SCcTpsrUVgiE9O3aPEMwCSPE8mJMtS3Oe8xcJPWY6%2Bo1wHRenHEueEjypCASntkk%2BVnL3SIb%2B%2BTfrYvq%2Bl7ersvHQaScFooFAnIlHh2VF9NXmpYinHEVOmv3ehuoz98uckn13DmWqQgHmppinHPkqfvHaRbgh70Ke8lnODlzqKiHDppinXPPOfHhmRfvYdR8mxnD3Xlz1QVXmpwQ%2BSflO%2BISa7XWjtRhSfnLfiaWqK%2BSmppinXPPOJjXa7mHntkhY2nffCsAqKCXDpABEDPPOJjXUxZCoKyxgV3tJR6vCQo6eSzzl1CKOkfYy8WNzAyRgfZtJLXl5QyigJ%2F4cnuBE4jzy8v5Z9M%2BDmZmfljH%2BcNbMhWURIjI2ZsET%2B997VvS4X6c5R40SUMcFhiMKonwMBjKSeg0ML5ZZWh3afrPYPTwXI%2F2BTsDKpqR2avYO25gM2HX5YN957zACQ6q6kpOegdJf2pSyhMRrAXC%2B91iF4ILJWP7BRMTMZR5jJVDbFqNO2UQJB8dIX7epc9B3TBBYEWNl1SlRvzxTls%2BnTZEfDSbdPZ35SScMS2j2qNZbDJUVrN69mixpnn%2FP1%2B3RPpzCr23x6FTn62hkh0iZDojLMq4Ess7S425K%2BB34UMyqlBLneBQwTVRZ1DYqSwp46SipFAcpQC1PrrbzD%2BxSWw4yjQ3%2B6Cg4K5GtgVeaHRCNPiSRSII%2Btm%2B3VG2dvTOnmxOgmQfOKqZM95qAROvR7felc4dn%2BS%2Fg2sGB6Wh4YJtJkurvKN5hosYTRvieWwMNJ%2F8E%2BUrD5YOnL3O6LROlzcSO3wv7STqOwwNOfw86F1eZwZrmWRiq9T3IqjLjdsWFzCdsFbLZkSObvZ9%2F49NRY%2Fldmy%2BQ7ss19qve6JPEGKymmAwAOlBLVGcUB0uHpUw0rxtlpdwuSRWk0z5j8T8K2nUMs1Xmak4xDaab6yDrWQ2Vaay4wH0eV5Q%2BQtnXv95jk0gwD6Ktmnt03VI%2B2vIkNplf8jAo63nMB2INqA47QdLNMRLsn7eXiv1oXvuN%2BoYEjMjvyg3cHVT8Xszp6aAm0hHDLYVBMDQa1ZtG1mIsk99TB3oZXZMNdrXZ3Qj%2Fjzr4Ccza8ms9Wpg9%2F2c%2Bef0xvXOR6wKs51f759XXYPSmK%2BuyT3CWwBcMaPvFPM4tYdSF6%2FD3x7KiJ%2FM7YbSxSie%2BhiLe3dfPv9LOYNgF4HXSWWDVZMu4zoLiMxMiX%2F%2FUVFYllCjPxgdVOcrUn7s0CnCkZfSZyyaXWTIrZt0RtVqixXcyqhOY6DK2lK4VFehGnyWdNH%2FqAngALDbIKD0Pn1iJ9yMIG3LTf42nYqfTKpy5UqOAiMbsVqkKq0n%22%2C%22p%22%3A%22%7B%5C%22ncbtn%5C%22%3A%5C%22795.5%7C188%7C42%7C30%7C188%7C218%7C795.5%7C837.5%5C%22%2C%5C%22umidToken%5C%22%3A%5C%22G0803760ADCBAE413601735598339560FA332DF3BD241DE82AD%5C%22%2C%5C%22ncSessionID%5C%22%3A%5C%225e701f13f8c3%5C%22%2C%5C%22et%5C%22%3A%5C%221%5C%22%7D%22%2C%22scene%22%3A%22register%22%2C%22asyn%22%3A0%2C%22lang%22%3A%22cn%22%2C%22v%22%3A1%7D&x5secdata=xd9063ba993fd20b0e546fdebaca1dec6ae16cd92dd71b2b1d1712903436a-1109984729a88757878abazc2aaa__bx__detail.1688.com%253A443%252Foffer%252Fpage%252Fdetail.htm&ppt=2&landscape=1&ts=1712903440709&v=0907786509839728',
    cookies=cookies,
    headers=headers,
)
print(response.cookies)
'https://detail.1688.com/offer/page/detail.htm/_____tmd_____/slide?slidedata={"a":"X82Y__0e1748d45e9398849fd9ba9e6eb0c705","t":"38e59cb41f7b1a66cbd80c6b0eb7c776","n":"227!SSiSphijqAIt4rhWcU3joDudZ+P4JL9j4lPPOrzYq/XWntR3DxnL3JrUVgiE9O3aPEMwCSPE8mJMtS3Oe8xcJPWY6+o1wHRenHEueEjypCASntkk+VnL3SIb++TfrYvq+l7ersvHQaScFooFAnIlHh2VF9NXmpYinHEVOmv3ehuoz98uckn13DmWqQgHmppinHPkqfvHaRbgh70Ke8lnODlzqKiHDppinXPPOfHhmkhuwbR8mxnD3Xlz1QVXmpwA+SOlOyi8aR36nz9klHnD3iSdqKoHZZvCnHEuOfvHaR3SHtR8l86IdhSL0QgHmppGcrCuOfvHaR8w3o7x5kfCy0vil3rkUMUL/qx3CAOCosOLcnOx5V+Gy0xQWA9xgf3AN4lNIrql/JODd+xCSVx89GJHXh/TzT1Lp1GlGew+6KQh+yFGO7iPKtQK8TJslKXpy8hebW4RfF7zgEEo0BTvpZzSJloZaZTrNUkDq8S7ZlfnrxGs0znTzTTDz9bHivJ3wJCU52GXa5/OdyDa4jbb5cdXKGlGgpKsA8jbzYDa2Mw6hu/pdC+OGdpSG0dKFFQbn2mrfzVtwOCaQiEg8ebLI2dxvAa0bvh4Wgg0FtkD9bZQF7lLXsgpUu17y0VLTT4SylGTUf29VLkG+RxDaUPc/BKkZ+Z/vZKCNA+yNpiGwiCx19eUSl8P4ueYjL+VbuZEOsDaWA8o7hXVUvcsfy3ieflaMZg5zKUDo9GI2KcDP8MpoqmaSLw33rR7KkhLHfqTgaB3uGp3yiOwC3sSAxb6rEo7uDk1z0WfraTXzn/v1fd0rYR8oIRQCdk64pJtA4S212/K0qzv4pVr+TBJ6IgrA+PZAFwoC9qJQ2uk4HOiupvdsAVzXvQ0wYNaWNiW3ADZ/o/fj3cXaKtFD64bLxiDTEypiXPDnK0nAAXa1uvhOHFWsYNvMTC2GB5W9YcXlvIx+dzIrkktlyzX07TK3jkfYLsz2lLvIv01EHDlqMhowZIeYniEgxlsuSlcIv80h4MoEyqawGhRV53zuixZookjRBUCsNHRlyZ1ldfmtmDsbs/k1yz6zXMsiQl9n2LFI4SAqiV9La91HqBzJywyR0ERg8dA5AUnXwVOtqrHNmMIkhiX4HPoOYyzCvUUav27tAclELdKYmWLdL9qTl7C+z959IJUDZ84ggjYUiDZ5HUriol7ZgZfZKZcGORTF9LksLUtF1ySpleP2iTLwxFBENMgEmBUpkqVeihBDQrgF7SRi9kmRkSTJlsyarFy8JqydDem4O0Zcxq7YNrstCi+ULlIJjjDKV5oheemQ3CxymuX9WaKIeZcbiSYXfK4rlJZLIY6EUQxZ/0jm0bom0B9USZ+t59EFtUFbfa9ADPjoy6uJpm4IjtwRXdZJH3rNfLTHUTPBPXc+4h8nmot74xCl20giLT0S8wiYO4hbo6iVwljV1RMKQQmNRzKBUg=","p":"{\"ncbtn\":\"795.5|245|42|30|245|275|795.5|837.5\",\"umidToken\":\"G77DF357D8FF87D332FC682C9915DEDCB19BB5DB06EA99D30ED\",\"ncSessionID\":\"5e701f13f8c3\",\"et\":\"1\"}","scene":"register","asyn":0,"lang":"cn","v":1}&x5secdata=xdd9bf4834132b47ab38e59cb41f7b1a66cbd80c6b0eb7c7761712908474a-1109984729a88757878abazc2aaa__bx__detail.1688.com%3A443%2Foffer%2Fpage%2Fdetail.htm&ppt=2&landscape=1&ts=1712908496815&v=02441309655714181'