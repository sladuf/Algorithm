# 21.02.12 [순위]

from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    #win = 내가 이긴애들
    #lose = 내가 진애들
    for a,b in results:
        win[a].add(b)
        lose[b].add(a)
        
    for i in range(1, n+1):
        for j in lose[i]:
            win[j].update(win[i])
        for j in win[i]:
            lose[j].update(lose[i])
            
    for i in range(1,n+1):
        if len(win[i])+len(lose[i]) == n-1:
            answer+=1
    return answer
