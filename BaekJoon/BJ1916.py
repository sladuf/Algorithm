# 21.03.09 [최소비용 구하기]
'''
최소->heap
출발지부터 시작해 방문한 노드들 중에 인접한 노드 사이의거리가 짧은걸 선택
도착지에 도착했다면 그만(조건 : 도착 못하는 경우X)
'''
import sys
from collections import defaultdict
import heapq

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

dic=defaultdict(list)
for i in range(m):
	x,y,z=map(int,sys.stdin.readline().split())
	#방향 그래프
	dic[x].append([y,z])

a,b=map(int,sys.stdin.readline().split())

visited=[False for x in range(n+1)]
#출발지부터 탐색
h=[(0,a)]
while h:
	cnt,x=heapq.heappop(h)
	#도착지에 도착하면 종료(최소 heap이기 때문에 가장 먼저 나온 도착지 정보가 최단거리임)
	if x==b:
		print(cnt)
		break

	#최단거리에 밀려 중간에 다른 경로로 방문했을 수 있다.
	if visited[x]:
		continue
		
	visited[x]=True
	for i,j in dic[x]:
		if not visited[i]:
			heapq.heappush(h,(cnt+j,i))
