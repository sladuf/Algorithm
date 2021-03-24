# 21.03.08 [트리의 지름]
'''
1967과 동일한 문제 

트리의 지름 공식 :
어떤 한 점에서 가장 먼 노드를 선택 (A)
그 노드(A)에서 가장 먼 노드를 선택 (B)
A와 B사이의 거리 = 가장 긴 지름
'''
import sys
from collections import defaultdict
from collections import deque

n=int(sys.stdin.readline())

dic=defaultdict(list)

for i in range(n):
	l=list(map(int,sys.stdin.readline().split()))
	a=l[0]
	l=l[1:]
	for i in range(1,len(l),2):
		dic[a].append([l[i-1],l[i]])

visited=[0 for x in range(n+1)]
visited[1]=1
q=deque([[1,0]])
while q:
	m,cnt=q.popleft()
	for x,y in dic[m]:
		if visited[x] == 0:
			q.append([x,cnt+y])
			visited[x]=cnt+y
visited[a]=0
a=1
for i in range(n+1):
	if visited[i]>visited[a]:
		a=i

visited=[0 for x in range(n+1)]
visited[a]=1
q=deque([[a,0]])
while q:
	m,cnt=q.popleft()
	for x,y in dic[m]:
		if visited[x] == 0:
			q.append([x,cnt+y])
			visited[x]=cnt+y
print(max(visited))
