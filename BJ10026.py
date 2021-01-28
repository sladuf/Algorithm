# 21.01.26 [적록색약]
import sys
import copy
from collections import deque

def RGB(pic):
    global people

    cp = copy.deepcopy(pic)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for a in range(n):
        for b in range(n):
            if cp[a][b] == 'R':
                queue = deque([[a,b]])
                cp[a][b] = 'A'
                people += 1
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        if 0<=xx<n and 0<=yy<n and cp[xx][yy] == 'R':
                            queue.append([xx,yy])
                            cp[xx][yy] = 'A';
    for a in range(n):
        for b in range(n):
            if cp[a][b] == 'G':
                queue = deque([[a,b]])
                cp[a][b] = 'A'
                people += 1
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        if 0<=xx<n and 0<=yy<n and cp[xx][yy] == 'G':
                            queue.append([xx,yy])
                            cp[xx][yy] = 'A';
    GB(cp)

def GB(pic):
    global people, RG_people

    cp = copy.deepcopy(pic)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for a in range(n):
        for b in range(n):
            if cp[a][b] == 'A':
                queue = deque([[a,b]])
                cp[a][b] = 'C'
                RG_people +=1
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        if 0<=xx<n and 0<=yy<n and cp[xx][yy] == 'A':
                            queue.append([xx,yy])
                            cp[xx][yy] = 'C';
    B_dfs(cp)

def B_dfs(pic):
    global people, RG_people

    cp = copy.deepcopy(pic)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for a in range(n):
        for b in range(n):
            if cp[a][b] == 'B':
                queue = deque([[a,b]])
                cp[a][b] = 'C'
                people +=1
                RG_people +=1
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        if 0<=xx<n and 0<=yy<n and cp[xx][yy] == 'B':
                            queue.append([xx,yy])
                            cp[xx][yy] = 'C';


n = int(sys.stdin.readline())
pic = []
people = 0
RG_people = 0
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    pic.append(temp)
RGB(pic)
if RG_people == 0:
    print(people, 1)
else:
    print(people, RG_people)
