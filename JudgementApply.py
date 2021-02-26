import requests as r
import json as js
from fake_useragent import UserAgent

checkurl='http://api.bilibili.com/x/credit/jury/requirement'
applyurl='http://api.bilibili.com/x/credit/jury/apply'
avaliability=False

def Apply(sessdata,csrf):
    headers={
        'cookie': 'SESSDATA={}'.format(sessdata),
        'Host': 'api.bilibili.com',
        'User-Agent': UserAgent(verify_ssl=False).random,
    }
    result=js.loads(r.get(checkurl,headers=headers).text)
    blocked,cert,level,rule=result['data']['blocked'],result['data']['cert'],result['data']['level'],result['data']['rule']
    if(not blocked and cert and level and rule):
        global avaliability
        avaliability=True
    headers={
        'cookie': 'bili_jct={}; SESSDATA={}'.format(csrf,sessdata),
        'Host': 'api.bilibili.com',
        'User-Agent': UserAgent(verify_ssl=False).random,
    }
    params={
        'csrf': csrf
    }
    if(avaliability):
        print('检测到未有风纪委员资格但具有申请资格，正在尝试申请……')
        result=js.loads(r.post(applyurl,headers=headers,params=params).text)
        print(result)
        if result['code']==0:
            returnmsg='申请成功'
            return True,returnmsg
        else:
            status={
                -101: '返回错误码-101，账号未登录，请检查sessdata和csrf是否有效',
                -111: '返回错误码-111，csrf校验失败，请检查csrf是否有效',
                25016: '返回错误码25016，当天的风纪委员资格已经发放完成'
            }
            returnmsg=status[result['code']]
            return False,returnmsg

