import requests as r
import json as js
from fake_useragent import UserAgent

url='http://api.bilibili.com/x/credit/jury/caseObtain'

def GetNew(csrf,sessdata):
    headers={
        'cookie': 'bili_jct={}; SESSDATA={}'.format(csrf,sessdata),
        'Host': 'api.bilibili.com',
        'User-Agent': UserAgent(verify_ssl=False).random,
    }
    params={
        'csrf': csrf
    }
    data=r.post(url,headers=headers,params=params)
    dataloads=js.loads(data.text)
    # print(dataloads)
    if(dataloads['code']==25014 or dataloads['code']==25008): return True
    result=dataloads['data']['id']
    return result
