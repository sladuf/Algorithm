# 21.02.11 [위장]
from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for a,b in clothes:
        dic[b]+=1
        
    for i in dic.values():
        answer *= (i+1)
    answer -= 1
    return answer