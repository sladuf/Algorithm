# 21.01.26 [트리의 부모 찾기]
import sys
from collections import defaultdict
from collections import deque


n = int(sys.stdin.readline())
tree = defaultdict(list)
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0 for x in range(n+1)]
queue = deque([1])

while queue:
    temp = queue.popleft()
    for i in tree[temp]:
        if result[i] == 0:
            result[i] = temp
            queue.append(i)

for i in range(2, n+1):
    print(result[i])
