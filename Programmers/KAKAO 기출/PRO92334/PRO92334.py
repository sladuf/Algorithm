# https://school.programmers.co.kr/learn/courses/30/lessons/92334

import sys
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    dic = defaultdict(list)
    cnt = defaultdict(int)
    
    for i in set(report):
        a,b = i.split(" ")
        dic[a].append(b)
        cnt[b] += 1
    
    for i in id_list:
        temp = 0
        for j in dic[i]:
            if cnt[j] >= k:
                temp+=1
        answer.append(temp)
    
    return answer