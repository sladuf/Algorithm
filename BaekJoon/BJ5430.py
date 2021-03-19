# 21.02.15 [AC]
import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    q = deque(list(sys.stdin.readline().strip('[]\n').split(',')))
    r = 0
    if n == 0 and 'D' in p:
        print('error')
        continue
    flag = True
    for j in p:
        if j == 'R':
            if r == 1:
                r=0
            else:
                r=1
        else:
            if q:
                if r==0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                flag = False
                break

    if flag == True:
        print('[', end='')
        if r==0:
            print(",".join(q), end='')
        else:
            print(','.join(reversed(q)),end='')
        print(']')
            
