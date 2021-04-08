def solution(a):
    answer = 0
    dp= [[0,0] for x in range(len(a))]
    
    l=a[0]
    for i in range(0,len(a)):
        if l>= a[i]:
            dp[i][0]=1
            l=a[i]
    r=a[-1]
    for i in range(len(a)-1, -1,-1):
        if r>=a[i]:
            dp[i][1]=1
            r=a[i]
    
    for i in range(0, len(a)):
        if sum(dp[i]) > 0:
            answer+=1
    return answer