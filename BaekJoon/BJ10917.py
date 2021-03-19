# 21.03.06 [Your life]
'''
BFS + 우선순위 Q
각자 연결된 꿈을 heap에 내림차순으로 넣는다. (N이 가장 크기 때문)
n이 나올때까지 bfs한다
'''
import sys
from collections import defaultdict
from collections import deque
import heapq


n,m = map(int, sys.stdin.readline().split())
dic=defaultdict(list)
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    #내림차순으로 heap에 넣음
    heapq.heappush(dic[a],-b)

res = -1
q=deque([[1,0]])
while q:
    num,cnt=q.popleft()
    for i in range(len(dic[num])):
        #내림차순으로 넣었으니까 나올 때 *-1
        temp = -1*heapq.heappop(dic[num])
        if temp == n:
            res=cnt+1
            break
        else:
            q.append([temp,cnt+1])
    if res != -1:
        break
print(res)
