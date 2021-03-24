# 21.03.24 [DNA]

import sys

n,m=map(int,sys.stdin.readline().split())
s=[]
for i in range(n):
    s.append(sys.stdin.readline().strip())

res=''
total=0
for i in range(m):
    dp=[0 for x in range(4)]
    for j in range(n):
        if s[j][i] == 'A':
            dp[0]+=1
        elif s[j][i] == 'C':
            dp[1]+=1
        elif s[j][i] == 'G':
            dp[2]+=1
        else:
            dp[3]+=1
    num=max(dp)
    temp=dp.index(num)
    if temp==0:
        res+='A'
    elif temp==1:
        res+='C'
    elif temp==2:
        res+='G'
    else:
        res+='T'
    total+=sum(dp)-num

print(res)
print(total)