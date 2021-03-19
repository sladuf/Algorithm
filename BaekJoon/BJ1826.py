# 21.02.25 [연료 채우기]
import sys
import heapq

n = int(sys.stdin.readline())
h = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    heapq.heappush(h,[a,b])

l, oil = map(int,sys.stdin.readline().split())

res = 0
t = []
while oil < l:
    while h:
        if h[0][0] <= oil:
            a,b = heapq.heappop(h)
            heapq.heappush(t,-b)
        else:
            break
    if t:
        a = -1*heapq.heappop(t)
        oil+=a
        res+=1
    else:
        break

if oil >= l:
    print(res)
else:
    print(-1)