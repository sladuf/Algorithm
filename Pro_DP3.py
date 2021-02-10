# 21.02.10 [등굣길]
def solution(m, n, puddles):
    mn = [[1]*m for x in range(n)]

    for x, y in puddles:
        mn[y-1][x-1] = 0
        #침수지역이 젤 왼쪽이면 그 아랫 부분은 다 0임
        if x-1 == 0:
            for i in range(y,n):
                mn[i][0] = 0
        #침수지역이 젤 위쪽이면 그 오른쪽 부분은 다 0임
        if y-1 == 0:
            for i in range(x,m):
                mn[0][i] = 0
                
    #오른쪽과 아래로만 이동 가능하므로 위쪽과 왼쪽에서 온 애들의 숫자를 +=
    for i in range(1,n):
        for j in range(1,m):
            if mn[i][j] == 0:
                continue
            mn[i][j] = mn[i-1][j] + mn[i][j-1]
            
    answer = mn[-1][-1]%1000000007
    return answer