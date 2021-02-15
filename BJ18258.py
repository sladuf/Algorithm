# 21.02.15 [큐 2] / Queue
import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()
for i in range(n):
    temp = sys.stdin.readline().strip().split()
    if temp[0] == 'push':
        q.append(int(temp[1]))
    elif temp[0] == 'pop':
        if q :
            print(q.popleft())
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(q))
    elif temp[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)