import requests
import urllib3
import pandas
import openpyxl


class Boss:
    def __init__(self, kw=None, pn=1, city=None):
        self.headers = {
            'Host': 'www.zhipin.com',
            'Connection': 'keep-alive',
            'ua': b'{"model":"microsoft","platform":"windows"}',
            'wt2': 'DILa1EBmukXDj1sjNOElrSSM - yRPhFps4gJBbtTnS94OkTmlQmxh4hWPbZEHzBaN0Ef5o_zqwF9KxJ5gdIxOX5w~~',
            'zpAppId': '10002',
            'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/98.0.4758.102Safari/537.36MicroMessenger/7.0.20.1781(0x6700143B)NetType/WIFIMiniProgramEnv/WindowsWindowsWechat/WMPFXWEB/6945',
            'Content-Type': 'application/x-www-form-urlencoded',
            'mpt': 'a93337936b6f6247b04324dc4a9b4153',
            'scene': '1145',
            'referer': 'https://servicewechat.com/wxa8da525af05281f3/446/page-frame.html',
            'xweb_xhr': '1',
            'x-requested-with': 'XMLHttpRequest',
            'miniappVersion': '5.0802',
            'platform': 'zhipin/windows',
            'ver': '5.0802',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross - site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh'

        }
        self.kw = kw
        self.detail = []
        self.pn = pn
        self.code = '100010000'
        self.city = city

    def paramas(self, pn=1):
        paramas = {
            'pageSize': '15',
            'query': f'{self.kw}',
            'city': f'{self.code}',
            'source': '1',
            'stage': '',
            'scale': '',
            'degree': '',
            'industry': '',
            'salary': '',
            'experience': '',
            'sortType': '0',
            'subwayLineId': '',
            'subwayStationId': '',
            'districtCode': '',
            'businessCode': '',
            'longitude': '',
            'latitude': '',
            'position': '',
            'expectId': '',
            'expectPosition': '',
            'page': f'{pn}',
            'appId': '10002',

        }
        url = 'https://www.zhipin.com/wapi/zpgeek/miniapp/search/joblist.json'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        data = requests.get(url=url, headers=self.headers, verify=False, params=paramas).json()
        self.data_to_detail(json_data=data)

    def data_to_detail(self, json_data=None):
        job_list = json_data['zpData']['list']
        i = 0
        for job_data in job_list:
            job_info = {
                'securityId': job_data['securityId'],
                'JobId': job_data['encryptJobId'],
                'lid': job_data['lid']
            }
            i += 1
            self.get_detail_data(info=job_info)
            print(f'第{i}条正在保存中')
        self.info_to_frame(infos=self.detail)

    def get_detail_data(self, info=None):
        paramas = {
            'securityId': info.get('securityId'),
            'jobId': info.get('JobId'),
            'lid': info.get('lid'),
            'source': '11',
            'scene': '',
            'appId': '10002'
        }
        url = 'https://www.zhipin.com/wapi/zpgeek/miniapp/job/detail.json'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        json_data = requests.get(url=url, headers=self.headers, params=paramas, verify=False).json()
        self.get_detail_info(data=json_data)

    def get_detail_info(self, data=None):
        info = {
            '职位名称': data['zpData']['jobBaseInfoVO']['positionName'],
            '分类': data['zpData']['jobBaseInfoVO']['positionCategory'],
            '薪资': data['zpData']['jobBaseInfoVO']['salaryDesc'],
            '学历': data['zpData']['jobBaseInfoVO']['degreeName'],
            '工作经验': data['zpData']['jobBaseInfoVO']['experienceName'],
            '工作区域': data['zpData']['jobBaseInfoVO']['locationDesc'],
            '工作地址': data['zpData']['jobBaseInfoVO']['address'],
            '岗位职责': data['zpData']['jobBaseInfoVO']['jobDesc'].replace('\n', ''),
            '公司名称': data['zpData']['brandComInfoVO']['comName'],
            '公司法人': data['zpData']['brandComInfoVO']['legalPerson'],
            '注册地址': data['zpData']['brandComInfoVO']['regAddress'],
            '成立时间': data['zpData']['brandComInfoVO']['startDate'],
            '注册资本': data['zpData']['brandComInfoVO']['regCapital'],
            '员工数量': data['zpData']['brandComInfoVO']['scaleName'],
            '业务范围': data['zpData']['brandComInfoVO']['businessScope'],
            '公司简介': data['zpData']['brandComInfoVO']['introduce']
        }
        if info:
            self.detail.append(info)

    def info_to_frame(self, infos=None):
        positionName = []
        positionCategory = []
        salaryDesc = []
        degreeName = []
        experienceName = []
        locationDesc = []
        address = []
        jobDesc = []
        comName = []
        legalPerson = []
        regAddress = []
        startDate = []
        regCapital = []
        scaleName = []
        businessScope = []
        introduce = []
        for data in infos:
            positionName.append(data['职位名称']),
            positionCategory.append(data['分类'])
            salaryDesc.append(data['薪资'])
            degreeName.append(data['学历'])
            experienceName.append(data['工作经验'])
            locationDesc.append(data['工作区域'])
            address.append(data['工作地址'])
            jobDesc.append(data['岗位职责'])
            comName.append(data['公司名称'])
            legalPerson.append(data['公司法人'])
            regAddress.append(data['注册地址'])
            startDate.append(data['成立时间'])
            regCapital.append(data['注册资本'])
            scaleName.append(data['员工数量'])
            businessScope.append(data['业务范围'])
            introduce.append(data['公司简介'])
        dataFrame = {
            '职位名称': positionName,
            '分类': positionCategory,
            '薪资': salaryDesc,
            '学历': degreeName,
            '工作经验': experienceName,
            '工作区域': locationDesc,
            '工作地址': address,
            '岗位职责': jobDesc,
            '公司名称': comName,
            '公司法人': legalPerson,
            '注册地址': regAddress,
            '成立时间': startDate,
            '注册资本': regCapital,
            '员工数量': scaleName,
            '业务范围': businessScope,
            '公司简介': introduce
        }
        self.info_to_excel(frame=dataFrame)

    def info_to_excel(self, frame=None):
        df = pandas.DataFrame(frame)
        df.to_excel(f'{self.kw}{self.city}.xlsx', engine='openpyxl', index=False)
        print(f'{self.kw}{self.city}保存完成')

    def get_page(self):
        for i in range(self.pn):
            print(f'正在采集第{i + 1}页数据......')
            self.paramas(pn=i + 1)

    def get_city_code(self):
        url = 'https://www.zhipin.com/wapi/zpCommon/miniapp/getCityData?appId=10002'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(url=url, headers=self.headers, verify=False).json()
        city_code = {}
        for data in response['zpData']['cityList']:
            for city in data['subLevelModelList']:
                city_code[city['name']] = city['code']
        code = city_code.get(f'{self.city}')
        if code:
            self.code = code
            self.get_page()
        else:
            print(f'输入的{self.city}不存在，请重新输入')


if __name__ == "__main__":
    boss = Boss(kw='python', pn=30, city='杭州')
    boss.get_city_code()
