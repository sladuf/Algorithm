# 2023.06.26

from collections import deque
def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    for i in range(len(queue1)*4):
        if sum1 == sum2:
            return i
        elif sum1 > sum2:
            temp = q1.popleft()
            q2.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            sum1 += temp
            sum2 -= temp
    return -1

'''
-- queue 완탐..?
0. queue1과 queue2의 합을 구해서 반복하기
1. 합이 더 큰 queue를 pop해서 작은 곳으로 append
2. q1,q2의 길이가 똑같으니까 q1*4만큼 반복하기
while로 하면 무한 반복 하는 경우 생길 수 있음
3. 반복문 안에서 같아지면 return answer하고
4. 반복문 밖으로 나왔으면 return -1
시간 복잡도 max = 300,000 * 4 = 1,200,000
'''