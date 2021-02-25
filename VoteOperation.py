import requests as r
import json as js
from fake_useragent import UserAgent
voteurl='http://api.bilibili.com/x/credit/jury/vote'

voteaction={
    'Break': 1,
    'Rule': 2,
    "GiveUp": 3,
    'Delete': 4
}

def Vote(opreation,cid,csrf,sessdata):
    headers={
        'cookie': 'SESSDATA={}'.format(sessdata),
        'Host': 'api.bilibili.com',
        'User-Agent': UserAgent().random,
    }
    params={
        'cid': cid,
        'vote': voteaction[opreation],
        'attr': 0,
        'csrf': csrf
    }
    VoteReturn=r.post(voteurl,params=params,headers=headers).text
    VoteResult=js.dumps(VoteReturn)
    return VoteResult
