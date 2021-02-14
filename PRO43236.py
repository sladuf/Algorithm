# 21.02.14 [징검다리]
def solution(distance, rocks, n):
    answer=0
    '''
    최솟값을 이분탐색으로 가정해서
    제거하는 바위의 갯수가 n개면 최솟값으로 인식하자
    '''
    left = 0
    right = distance
    rocks.sort()
    while left<=right:
        mid = (left+right)//2
        remove = 0
        temp = 0
        for rock in rocks:
            if rock - temp < mid:
                remove+=1
            else:
                temp = rock
            if remove > n:
                break
                
        if remove>n:
            right=mid-1
        else:
            answer = mid
            left=mid+1
    return answer