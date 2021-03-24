# 21.02.23 [좋은 수열]
import sys

def ch(cnt):
    for i in range(1,cnt//2+1):
        if res[cnt-i:cnt] == res[cnt-(2*i):cnt-i]:
            return False

    if cnt == n:
        for i in res:
            print(i, end='')
        return True

    for i in range(1,4):
        if res[-1] == i:
            continue
        res.append(i)
        if ch(cnt+1):
            return True
        res.pop()

n = int(sys.stdin.readline())
res = [1]
ch(1)
