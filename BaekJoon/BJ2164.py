# 21.02.15 [카드2]

import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([x for x in range(1,n+1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())


print(queue[0 
