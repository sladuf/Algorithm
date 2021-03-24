# 21.02.10 [정수 삼각형]

import copy

def solution(t):
    answer = 0
    sum_t = copy.deepcopy(t)
    #위에서 온 값이 더 큰것을 선택해서 내려감
    for i in range(len(t)-1):
        for j in range(len(t[i])):
            if sum_t[i][j] + t[i+1][j] > sum_t[i+1][j]:
                sum_t[i+1][j] = sum_t[i][j] + t[i+1][j]
            if sum_t[i][j] + t[i+1][j+1] > sum_t[i+1][j+1]:
                sum_t[i+1][j+1] = sum_t[i][j] + t[i+1][j+1]
    answer = max(sum_t[-1])
    return answer
