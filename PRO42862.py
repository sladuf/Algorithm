# 21.02.08 [체육복]
def solution(n, lost, reserve):
    answer = 0
    students = [1 for x in range(n+1)]
    #잃어버린애 0 | 두개인데 잃어버린애 1 | 두개인애 2
    for i in lost:
        students[i] = 0
    for i in reserve:
        if students[i] == 0:
            students[i] =1
        else:
            students[i] = 2
    students[0] = 0
    #잃어버린애 중에 앞뒤로 2개인애가 있으면 가져옴
    for i in range(1, n+1):
        if students[i] == 0:
            if students[i-1] == 2:
                students[i-1] =1
                students[i] = 1
            elif i < n and students[i+1]==2:
                students[i+1]=1
                students[i]=1
    
    for i in students:
        if i >= 1:
            answer +=1
    return answer
