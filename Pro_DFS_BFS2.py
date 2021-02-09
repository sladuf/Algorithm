# 21.02.09 [네트워크]
from collections import deque
def solution(n, computers):
    def bfs(com):
        visited[com] = True
        queue = deque()
        queue.append(com)
        #queue로 연결되어 있는 컴퓨터 모두 visited=Ture
        while queue:
            com = queue.popleft()
            for i in range(n):
                if computers[com][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i] == True:
            continue
        #bfs를 새로 한다면 연결되지 않은 컴퓨터가 존재한다는 뜻
        bfs(i)
        answer+=1
        
    return answer