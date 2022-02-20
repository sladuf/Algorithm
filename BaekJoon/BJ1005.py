# 22.02.18 [ACM Craft]

import sys
from collections import defaultdict, deque

def input():
    return sys.stdin.readline()

t=int(input())
for tc in range(t):
    n,k = map(int, input().split())
    time = list(map(int, input().split()))
    dic = defaultdict(list)
    # degree는 진입가능한 선의 갯수를 나타냄
    degree = [0] * n
    for i in range(k):
        a,b = map(int,input().split())
        dic[a-1].append(b-1)
        degree[b-1] += 1
    w = int(input())
    q = deque()
    res = [0] * n
    for i in range(n):
        if degree[i] == 0:
            q.append(i)
            res[i] = time[i]
    while q:
        temp = q.popleft()
        for i in dic[temp]:
            if degree[i]:
                res[i] = max([res[i], res[temp] + time[i]])
                degree[i] -=1
            if degree[i] == 0:
                q.append(i)

    print(res[w-1])