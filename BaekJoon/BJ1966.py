# 21.02.13 [프린터 큐]
import sys
from collections import deque

t=int(sys.stdin.readline())

for i in range(t):
    n,m = map(int,sys.stdin.readline().split())
    temp = list(map(int,sys.stdin.readline().split()))
    queue = deque([])
    for i in range(n):
        queue.append([i,temp[i]])
    answer = 0
    while queue:
        pop = queue.popleft()
        if pop[1] >= max(temp):
            answer+=1
            temp[pop[0]] = 0
            if pop[0] == m:
                print(answer)
                break
        else:
            queue.append(pop)