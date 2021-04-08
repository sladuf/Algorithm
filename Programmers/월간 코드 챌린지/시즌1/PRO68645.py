def solution(n):
    answer = [[1]*x for x in range(1,n+1)]
    d=[[1,0],[0,1],[-1,-1]]
    now=0
    x=-1
    y=0
    num=0
    
    for i in range(n,0,-1):
        for j in range(0,i):
            x+=d[now][0]
            y+=d[now][1]
            num+=1
            answer[x][y]=num
        now+=1
        if now==3:
            now=0
    
    res=[]
    for r in answer:
        res+=r
    return res