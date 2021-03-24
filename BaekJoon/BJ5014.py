# 21.03.07 [스타트링크]
'''
1층부터 F층까지 visited을 체크해서
현재 강호가 있는 층+u -d을 통해 g로 갈 수 있는지 파악함
visited => (먼저 방문했다면 무조건 cnt가 낮으니까 방문한거 방문할 필요 X)
'''
import sys
from collections import deque

f,s,g,u,d=map(int,sys.stdin.readline().split())

res=-1
visited=[False for x in range(f+1)]
q=deque([[s,0]])
while q:
	now,cnt=q.popleft()
	if now==g:
		res=cnt
		break
	#f층을 넘을 수 없고, 1층보다 아래로 갈 수 없다.
	if now+u<=f and not visited[now+u]:
		visited[now+u]=True
		q.append([now+u,cnt+1])
	if now-d>=1 and not visited[now-d]:
		visited[now-d]=True
		q.append([now-d,cnt+1])
		
if res==-1:
	print("use the stairs")
else:
	print(res)
