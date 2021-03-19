# 21.02.20 [매칭 점수]

from collections import defaultdict
import re

def solution(word, pages):
    url = []
    body = []
    link = defaultdict(list)
    
    for p in pages:
        u = p.split('<meta property="og:url" content="https://')[1].split('"/>')[0]
        url.append(u)
        #a-z여집합을 .으로 바꾸고 .을 기준으로 split해서 word를 센다
        b = int(re.sub('[^a-z]', '.', p.lower()).split('.').count(word.lower()))
        body.append(b)
        l = p.split('<a href="')
        for x in l:
            if x.startswith('https://'):
                temp = x.split('https://')[1].split('">')[0]
                link[u].append(temp)
                
    res = [x for x in body]
    for i in range(len(url)):
        for j in link[url[i]]:
            if j in url:
                idx = url.index(j)
                res[idx] += (body[i]/len(link[url[i]]))
                
    return res.index(max(res))
