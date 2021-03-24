# 21.01.27 [알파벳]
import sys

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(x,y, cnt):
	global result
	result = cnt
	for i in range(4):
		xx=dx[i]+x
		yy=dy[i]+y
		if 0<=xx<r and 0<=yy<c and visited[ord(board[xx][yy])-65] == 0:
			visited[ord(board[xx][yy])-65] = 1
			result = max(result, bfs(xx,yy,cnt+1))
			visited[ord(board[xx][yy])-65] = 0
	return result

r,c = map(int, sys.stdin.readline().split())
board =[]
for i in range(r):
	temp = list(sys.stdin.readline().strip())
	board.append(temp)

result = 1
visited = [0 for x in range(26)]
visited[ord(board[0][0])-65] = 1
bfs(0,0,1)

print(result)
