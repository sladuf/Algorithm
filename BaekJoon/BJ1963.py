# 21.03.06 [소수 경로]
'''
BFS+DP
한개씩 바꿔서 Q에 넣고 바꿀 숫자와 일치하면 그만하기
소수는 에라토스테네스의 체로 미리 구해놓음

(Impossible이 나오는 경우가 있을까..?)
'''
import sys
from collections import deque

#소수가 저장되어있는 dp
dp=[True for x in range(10000)]

for i in range(2,501):
	if dp[i]:
		for j in range(i*i,10000,i):
			dp[j]=False

t=int(sys.stdin.readline())

for case in range(t):
	a,b=map(int,sys.stdin.readline().split())
	q=deque([[a,0]])
	res=-1
	#방문한 숫자는 다시 방문 X하기위해 visited 확인
	visited=[False for x in range(10000)]
	visited[a]=False
	while q:
		num,cnt=q.popleft()
		if num==b:
			res=cnt
			break
		num=str(num)
		#네자리 숫자니까 4번 반복 (각 자리수 마다 바꿔줌)
		for i in range(4):
			for j in map(str,range(10)):
				#첫번째 자리에는 0이 올 수 없음!!!
				if i==0 and j=='0':
					continue
				#i번째 수를 j로 바꾸는 코드
				temp=int(num[:i]+j+num[i+1:])
				#소수이면서 방문한 숫자가 아니면 Q에 삽입!
				if dp[temp] and not visited[temp]:
					q.append([temp,cnt+1])
					visited[temp]=True

	if res == -1:
		print('Impossible')
	else:
		print(res)
