import sys, heapq

n = int(sys.stdin.readline())

hq = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        heapq.heappush(hq, temp[j])
        if len(hq) > n :
            heapq.heappop(hq)

print(heapq.heappop(hq))