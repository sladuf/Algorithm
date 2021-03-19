# 21.03.07 [문자판]
'''
0==False는 True라는 엄청난 사실...때문에 질질끌었던 문제ㅜ
메모제이션을 생성된 문자열의 길이 마다 일일히 해줘야 한다.
계속 마지막만 체크해줬는데 시간초과가 났다.

알고리즘은 DFS+DP
'''
import sys

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(x,y,now):
	if now==l:
		return 1
		
	#이 전에 방문 한 경로에 포함된다면 더 이상 검사 X
	if dp[x][y][now] != -1:
		return dp[x][y][now]

	#지금 방문했으니까 0으로 변경(방문 X는 -1)
	dp[x][y][now]=0
	for i in range(1,k+1):
		for j in range(4):
			xx=dx[j]*i+x
			yy=dy[j]*i+y
			if 0<=xx<n and 0<=yy<m and s[xx][yy]==word[now]:
				#dp의 값은 다음 알파벳으로 dfs한 결과이다.
				dp[x][y][now] += dfs(xx,yy,now+1)
	return dp[x][y][now]

n,m,k=map(int,sys.stdin.readline().split())
s=[]
for i in range(n):
	s.append(list(sys.stdin.readline().strip()))
word=sys.stdin.readline().strip()
l=len(word)

#st는 시작할 인덱스를 담고있다. 즉 word의 첫번째 알파벳과 일치하는 index
st=[]
for i in range(n):
	for j in range(m):
		if s[i][j]==word[0]:
			st.append([i,j])

#방문한 적 없으면 -1 있으면 결과까지 도달한 횟수를 저장
dp=[[[-1]*l for x in range(m)] for y in range(n)]
res=0
for x,y in st:
	res+=dfs(x,y,1)
print(res)