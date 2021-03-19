# 21.02.20 [히스토그램에서 가장 큰 직사각형]
import sys

while True:
    h = list(map(int, sys.stdin.readline().split())) + [0]
    if h[0] == 0:
        break
    n = h[0]
    stack = [(1,h[1])]
    res = 0
    for i in range(2,n+2):
        w = i
        while stack and stack[-1][1] > h[i]:
            w, hi = stack.pop()
            res = max(res, (i-w)*hi)
        stack.append((w, h[i]))
    print(res) 
