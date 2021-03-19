# 21.02.12 [가장 먼 노드]
from collections import defaultdict
from collections import deque
def solution(n, edge):
    answer = []
    dic  = defaultdict(list)
    visited = [False for x in range(n+1)]
    for a,b in edge:
        dic[a].append(b)
        dic[b].append(a)
    
    queue = deque([[1,0]])
    visited[1] = True
    while queue:
        temp, now = queue.popleft() 
        ch = 0
        for i in dic[temp]:
            if visited[i] == False:
                queue.append([i,now+1])
                visited[i] = True
                ch +=1
        if ch == 0:
            answer.append(now)
    answer = answer.count(max(answer))
    return answer