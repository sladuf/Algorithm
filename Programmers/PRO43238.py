# 21.02.13 [입국심사]

def solution(n, times):
    answer = 0
    '''
    이분탐색 -> 젤 오래걸리는시간과 젤 적게 걸리는 시간을 이분탐색 하쟈
    '''
    left = 1
    right = max(times)*n
    
    while left<=right:
        mid = (left+right)//2
        p = 0
        for i in times:
            p+=mid//i
            
        #이분탐색 !!! 잘 봐두기 
        if p>=n:
            right=mid-1
            answer=mid
        else:
            left=mid+1
            
    return answer
