import pprint

import execjs
import requests
url = 'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id=646de0d00000000014026c89&cursor=&top_comment_id=&image_formats=jpg,webp,avif'
cookies = {
    'abRequestId': 'fb038d7b-5294-5e73-9751-05b7babdcfb8',
    'webBuild': '4.5.1',
    'a1': '18e2dc822e1vxm1am9hdmvg2j5lm7lmgjqqb7hfqm50000350567',
    'webId': '398c23fe914198ad7a497cea30218929',
    'websectiga': '2a3d3ea002e7d92b5c9743590ebd24010cf3710ff3af8029153751e41a6af4a3',
    'sec_poison_id': '60834dae-e40d-47f8-8777-04ba487f1541',
    'web_session': '030037a2dc582739a47e184a97224acb71f81d',
    'gid': 'yYdJfSYJS0VJyYdJfSYJJAxidyhC6y06jxf6AA6hkJV21D286W16kW888q282KW8Sjj4yiKj',
    'xsecappid': 'xhs-pc-web',
}
xs = execjs.compile(open("xhs.js",encoding='utf-8').read()).call('xs','/'.join(url.split('/')[3:]))
headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'abRequestId=fb038d7b-5294-5e73-9751-05b7babdcfb8; webBuild=4.5.1; a1=18e2dc822e1vxm1am9hdmvg2j5lm7lmgjqqb7hfqm50000350567; webId=398c23fe914198ad7a497cea30218929; websectiga=2a3d3ea002e7d92b5c9743590ebd24010cf3710ff3af8029153751e41a6af4a3; sec_poison_id=60834dae-e40d-47f8-8777-04ba487f1541; web_session=030037a2dc582739a47e184a97224acb71f81d; gid=yYdJfSYJS0VJyYdJfSYJJAxidyhC6y06jxf6AA6hkJV21D286W16kW888q282KW8Sjj4yiKj; xsecappid=xhs-pc-web',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'x-b3-traceid': 'cc8e877a329fecca',
    'x-s': xs,
    'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHFN0L1PaHVHdWMH0ijP/YSPfz0weHU8/b92BFlGnFEyBzT4fqUy0pVJ/4VJn4xqgbj+9YfqnFMPeZIPePMPeL9+UHVHdW9H0il+ArIP/GMPeDIweqENsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QJLp7/pziJLEg/gkwpM83/M4QPLMx874ypbpC/gk8+LMgz/z8yfqFnDz++pkgafT+2D83nSz+PpkxzfT8PS8k/nMnyDRgn/zwzF8T/fk8PFMgLgY+2Sk3/gkVybSCzfYwzMpC/LzzPMkxJBYwpbph/Fz3PFEr8BSyzFFF/nk8PLMo//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/S482rETnfMyprDI/Lz32rEC8AmypMDlnDz8PDMo//zwzMQknpzwypkxyAmyzrph/dkaJLRrpfMyySpE/gkiyDEozgk8pFki//Q8PDETL/zwJL83nnkpPrhUpfY+JLFUnnk02DExa/QyzF83/nk+PLMg/g4wpMLAnfkyJrFUzfM+zFk3nDz+2LEx8BSyzFkxn/QtJLMong4+pbkinS4bPpkLc/mwyD8T/dkwybDULfM+2DMC/L4p2LETz/p8yD8T/Lz+2DRgnfMyzFFU/nMQ+LMgLfYwJLFI/0QyyDRrL/z+yDDM/SziyMSLL/+yzbkx/fMz+LRr/gk+JLki/Lznypk/a0DjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J9p/8db8aob7JeQl4epsPrz6ag8+2DRyLgbypdq7agYO8pzl47HFqgzkanTU/FSkN7+3G9+haL+P8rDA/9LI4gzVPDbrnd+P4fprLFTALMm7+LSb4d+k4gzt/7b7wrQn498cqBzSprzg/FSh+b8QygL9nSm7GSmM4epQ4flY/BQdqA+l4oYQ2BpAPp87arS34nMQyFSE8nkdqMS1z9ly8B4A8S8F4oQUa9LIagrEGLQNqAmyqDYQP94S8SmFnDSbJ9p84gzmq7kgpLR6pD4Q4f4SygbFcUR889phySi3anYr8LSbypbzpL4pagYTLrRCJnMQyn+G8pm7wLSeLeLh8fzAnnP6qAbc49zQ4DbS8BEm8/mpLfpQyApApBQopgSM47YQyLTSPURO8p8/Po+3qg4lGfq6qM4M4opQ2bkY/Bbd8/ml4rbPwLRApM87/FShapkQcMmVJSmFa94n49pAcSi6woQOqMSS/7+nqgchanS6q9zpP7+nzoLIanSw8p488npLGpQVanT9qM+l47zQypQVqpmFL/Qn4BYQ40pSPMmFcFSk/fLl4g4kaLptq9kM4bQ74g4cqSm7zrDAybYQ2opUaf4QcL4VN7+kqgz+anYr4rSk8np84gzGaFS0qsHVHdWEH0iM+AcU+Ar7+AqVHdWlPsHCPA+R',
    'x-t': '1710165090879',
}

response = requests.get(
    'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id=646de0d00000000014026c89&cursor=&top_comment_id=&image_formats=jpg,webp,avif',
    cookies=cookies,
    headers=headers,
)
print(response.json())