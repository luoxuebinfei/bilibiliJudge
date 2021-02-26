import requests as r
from fake_useragent import UserAgent

caseurl='http://api.bilibili.com/x/credit/jury/caseInfo'

def GetCase(cid):
    params={'cid': cid}
    headers={
        'Host': 'api.bilibili.com',
        'User-Agent': UserAgent(verify_ssl=False).random,
    }
    info=r.get(caseurl,headers=headers,params=params)
    return info
