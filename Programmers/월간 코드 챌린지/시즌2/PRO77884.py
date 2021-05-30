def func(num):
    res = 1
    for i in range(1,num):
        if num%i == 0:
            res+=1
    if res%2==0:
        return num
    else:
        return -num

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer+=func(i)
        
    return answer