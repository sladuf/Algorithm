# 21.03.07 [퍼즐]
'''
2251번 문제와 매우 비슷
3*3 판이라서 완탐해도 상대적으로 반복이 적다!
앞으로 문제보고 어떤 알고리즘으로 해결 해야할지 모르겠으면 완탐으로 시도해야겠다..

받은 숫자들을 문자열로 두고 '1234567890'이 될 때까지
빈칸(0)을 상하좌우로 옮김
이미 옮겨서 만들었던 문자열이라면 pass 
'''
import sys
from collections import deque
from collections import defaultdict

m=''
for i in range(3):
	m+=sys.stdin.readline().strip().replace(' ','')

res=-1
#문자열을 저장할 딕셔너리(방문한적 있는 문자열이면 True)
dic=defaultdict(bool)
dic[m]=True
q=deque([[m,0]])
while q:
	n,cnt=q.popleft()
	if n=='123456780':
		res=cnt
		break
	idx=n.find('0')
	#idx는 0이 있는 index이다. 이를 기준으로 상하좌우 이동
	#q에 넣기전에 방문했는지 검사하고 넣는다.

	#UP(젤 첫번째 줄 0 1 2에 있다면 이동 X)
	if idx>=3:
		up=list(n)
		up[idx],up[idx-3]=up[idx-3],up[idx]
		up=''.join(up)
		if not dic[up]:
			q.append([up,cnt+1])
			dic[up]=True
	#DOWN(젤 마지막 줄 6 7 8에 있다면 이동 X)
	if idx<6:
		down=list(n)
		down[idx],down[idx+3]=down[idx+3],down[idx]
		down=''.join(down)
		if not dic[down]:
			q.append([down,cnt+1])
			dic[down]=True
	#RIGHT(젤 오른쪽 2 5 8에 있다면 이동 X)
	if idx%3!=2:
		r=list(n)
		r[idx],r[idx+1]=r[idx+1],r[idx]
		r=''.join(r)
		if not dic[r]:
			q.append([r,cnt+1])
			dic[r]=True
	#LEFT(젤 왼쪽 0 4 7에 있다면 이동 X)
	if idx%3!=0:
		l=list(n)
		l[idx],l[idx-1]=l[idx-1],l[idx]
		l=''.join(l)
		if not dic[l]:
			q.append([l,cnt+1])
			dic[l]=True
print(res)