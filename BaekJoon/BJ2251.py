# 21.03.07 [물통]
'''
1525번 문제와 매우 비슷
완탐은 경우의 수를 잘 체크하는게 중요한듯
여기서는 물통의 물을 옮기는 경우의 수를 잘 따져봐야함 (옮길 물통의 부피 고려 등등)
'''
import sys
from collections import defaultdict
from collections import deque

a,b,c=map(int, sys.stdin.readline().split())

#같은 경우를 또 탐색하면 시간낭비 오지니까 visited로 관리
visited=[[[False]*201 for x in range(201)] for y in range(201)]
#옮기다보니 다른 방법으로 같은 값이 나올 수 있으므로 set으로 설정해줌 
res=set()
q=deque([])
q.append([0,0,c])
while q:
	x,y,z=q.popleft()
	if visited[x][y][z]:
		continue

	#일일히 visited 체크하기 어려우니까 일단 q에 넣은다음에 check..
	visited[x][y][z]=True

	if x==0:
		res.add(z)
	'''
	옮길 물 통의 부피와 이미 갖고 있는 물의 양을 고려해서 옮겨야함
	'''
	#a->b
	if x+y<=b:
		q.append([0,x+y,z])
	else:
		q.append([x-(b-y),b,z])
	#a->c
	if x+z<=c:
		q.append([0,y,x+z])
	else:
		q.append([x-(c-z),y,c])

	#b->a
	if x+y<=a:
		q.append([x+y,0,z])
	else:
		q.append([a,y-(a-x),z])
	#b->c
	if y+z<=c:
		q.append([x,0,y+z])
	else:
		q.append([x,y-(c-z),c])

	#c->a:
	if x+z<=a:
		q.append([x+z,y,0])
	else:
		q.append([a,y,z-(a-x)])
	#c->b:
	if y+z<=b:
		q.append([x,y+z,0])
	else:
		q.append([x,b,z-(b-y)])

		
for i in sorted(res):
	print(i,end=' ')

