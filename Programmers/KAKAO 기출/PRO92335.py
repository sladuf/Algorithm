# https://school.programmers.co.kr/learn/courses/30/lessons/92335

import math

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def nTok(n,k):
    result = []

    while n > 0:
        mod = n%k
        n = n//k
        result.append(str(mod))

    result.reverse()
    return result


def solution(n, k):
    answer = 0

    knum = nTok(n, k)
    knum = ''.join(knum).split('0')

    for num in knum:
        if num == '':
            continue
        if isPrime(int(num)):
            answer+=1

    return answer

n = 437674
k = 3
print(solution(n, k))