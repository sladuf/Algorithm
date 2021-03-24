# 21.02.15 [오큰수]
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
nge = [-1 for x in range(n)]

stack = []
for i in range(n-1, -1, -1):
    while stack:
        if stack[-1] > a[i]:
            nge[i] = stack[-1]
            stack.append(a[i])
            break
        else:
            stack.pop()

    if not stack:
        stack.append(a[i])

for i in nge:
    print(i, end=' ')

