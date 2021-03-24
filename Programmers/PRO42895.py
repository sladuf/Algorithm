# 21.02.10 [N으로 표현]

def solution(N, number):
    answer = 0
    dic = {}
    if number == N:
        return 1
    #8번넘으면 return -1 이니까 8까지만 검사하자
    for i in range(1, 9):
        dic[i] = [int(str(N)*i)]

    for i in range(2, 9):
        a = 1
        b = i-1
        #모든 경우를 합집합으로 사칙연산함
        #ex)4면 1+3 2+2 3+1 1*3 2*2 3*1 ...
        while b>=1:
            for x in dic[a]:
                for y in dic[b]:
                    dic[i].append(x+y)
                    dic[i].append(x-y)
                    dic[i].append(x*y)
                    #0은 나누면 INF
                    if y != 0:
                        dic[i].append(x//y)
            if number in dic[i]:
                return i
            a+=1
            b-=1
            
    return -1
