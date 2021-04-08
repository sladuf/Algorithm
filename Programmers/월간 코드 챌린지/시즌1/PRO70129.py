def solution(s):
    cnt=0
    zero=0
    while s != '1':
        x=s.count('1')
        zero+= len(s)-x
        s=bin(x)[2:]
        cnt+=1
    
    return [cnt,zero]