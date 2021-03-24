# 21.01.26 [촌수계산]
import sys

def dfs(a, b, c):
    global result
    if a == b:
        result = c
        return
    while bro[a] :
        temp = bro[a].pop()
        if temp not in visited:
            stack.append(temp)
            visited.append(temp)
            dfs(temp, b, c+1)
    stack.pop()

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

bro = [[] for x in range(0, n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    bro[x].append(y)
    bro[y].append(x)

stack = [a]
visited = [a]
result = -1
dfs(a, b, 0)

print(result)

