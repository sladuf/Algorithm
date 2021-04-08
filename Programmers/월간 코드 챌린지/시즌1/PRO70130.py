answer=[0,0]
def qt(arr, n, x,y):
    temp=arr[x][y]
    flag=True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if temp != arr[i][j]:
                flag=False
        if not flag:
            break
    if flag:
        answer[temp]+=1
    else:
        qt(arr, n//2, x,y)
        qt(arr, n//2, x,y+n//2)
        qt(arr, n//2, x+n//2, y)
        qt(arr, n//2, x+n//2, y+n//2)

def solution(arr):
    global answer
    qt(arr,len(arr),0,0)
    
    return answer