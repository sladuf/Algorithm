# 21.02.15 [요세푸스 문제 0] / Queue
import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
queue = deque([x for x in range(1, n+1)])

print('<', end='')
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())

    print(queue.popleft(),end='')
    if queue :
        print(',', end=' ')
print('>')