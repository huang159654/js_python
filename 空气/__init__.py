import re

import requests

# cookies = {
#     'Hm_lvt_6088e7f72f5a363447d4bafe03026db8': '1688458232',
#     'Hm_lpvt_6088e7f72f5a363447d4bafe03026db8': '1688460353',
# }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_6088e7f72f5a363447d4bafe03026db8=1688458232; Hm_lpvt_6088e7f72f5a363447d4bafe03026db8=1688460353',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'city': '上海',
}

response = requests.get(
    'http://www.aqistudy.cn/historydata/monthdata.php',
    params=params,
    # cookies=cookies,
    headers=headers,
    verify=False,
).text
# print(response)
url_id=re.findall('\<li\>\<a href\=\"(.*?)\?city\=(.*?)\&month\=(.*?)\"\>(.*?)\<\/a\>\<\/li\>',response)#提取url
# print(url_id)
for id in url_id:
    sah=id[1]
    sa=id[0]
    id_url='http://www.aqistudy.cn/historydata'+id[0]
    # print(id_url)
    params1 = {
        'city': '上海',
        'month': sah,
    }
    data = {
        'hH8MerJfc': 'aoai4TebSTEoHhgDly1MwM70muBClHHhpEhHIvbMhSPPufjjK1y8lhrvPNMMjRhLEzV6OC+TcUu3Bc2wqA1J/x7uBgf00i8oA1XOdDhBYwihS0jwQB8rz/UDTlGYMo0Rfg6s2RWjZKxvCAemuzxgBFD8g/Go8meYuhMcN7pQeY6huqkjOBBkoiSE/Z9QxFRQ77X9PGl5IAzriHHBp5bNhg/FOsBhHQFICj2/9oFaisLLzby0CUELOYKF2vg1OkinYSuBxmeo3hkZhFLudXWGanBXRfxgUj2aAYlxARSTJbGjpoyzZIY2rYMxXvlgkOnGymXPr9c1hzswPHjpEPW+8SMK+cZgh1dqw/lcQQ3/mnM=',
    }

    response1 = requests.post('https://www.aqistudy.cn/historydata/api/historyapi.php', headers=headers, data=data).text
    print(response1)
    print(id_url,sah)
    break