# Olympiad Pizza
# 2023.05.02

import sys
from collections import deque

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split(" ")))
line = deque([(cnt,i) for i, cnt in enumerate(line)])

result = [0 for _ in range(n)]
now = 1
while line:
    cnt, idx = line.popleft()
    if cnt == 1:
        result[idx] = str(now)
    else:
        line.append((cnt-1,idx))
    now+=1
print(" ".join(result))