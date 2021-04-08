def solution(n):
    answer = 0
    arr=[]
    while n>0:
        arr.append(n%3)
        n//=3
    
    for idx,i in enumerate(reversed(arr)):
        answer+=i*(3**idx)
        
    return answer