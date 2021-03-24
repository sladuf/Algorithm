# 21.02.15 [주유소] / Greedy
import sys

n = int(sys.stdin.readline())
length = list(map(int,sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

now = cost[0]
result = 0
for i in range(len(length)):
    if now > cost[i]:
        now = cost[i]
    result+=(now*length[i])
    
print(result)
