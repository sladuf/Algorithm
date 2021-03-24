# 21.02.17 [K번째 수]
'''
생각하는거 진짜 개어려움 ㅜㅜ
정렬하지 않고 최솟값을 찾는게 포인트
'''
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

l = 1
r = k #k보다 큰수가 k번째에 올 수가 없음 (1,2,2,3,3...)
result = 0
while l<=r:
    mid = (l+r)//2
    m = 0
    for i in range(1,n+1):
        if mid//i == 0:
            break
        m += min(mid//i,n)

    if m >= k:
        r = mid-1
        result = mid
    else:
        l = mid+1
        
print(result)
