from collections import defaultdict

def solution(table, languages, preference):
    answer = ''
    dic = defaultdict(int)
    for a,b in zip(languages, preference):
        dic[a] = b
    
    res = defaultdict(int)
    for temp in table:
        num = 5
        temp = temp.split()
        for i in range(1,5+1):
            res[temp[0]] += (num*dic[temp[i]])
            num-=1
    
    total = 0
    for k in res.keys():
        if total < res[k]:
            total = res[k]
            answer = k
        if total == res[k]:
            answer = sorted([answer,k])[0]
    
    return answer
