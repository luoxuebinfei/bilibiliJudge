import requests as r
import json as js
from fake_useragent import UserAgent

url='http://api.bilibili.com/x/credit/jury/jury'

def GetInfo(SESSDATA):
    test='SESSDATA={}'.format(SESSDATA)
    headers={
        'cookie': test,
        'Host': 'api.bilibili.com',
        'User-Agent': UserAgent().random,
    }
    info=r.get(url,headers=headers)
    info_loads=js.loads(info.text)
    status={
        1: '具有资格',
        2: '资格失效'
    }
    #print(info_loads)
    parsed=str({
        '用户名': info_loads['data']['uname'],
        '已裁决案件数': info_loads['data']['caseTotal'],
        '资格状态': status[info_loads['data']['status']],
        '剩余资格天数': info_loads['data']['restDays'],
        '裁决准确率': str(info_loads['data']['rightRadio'])+'%'
    })
    
    return info_loads,parsed

#GetInfo("581fcc29%2C1629713738%2C2f413%2A21")
