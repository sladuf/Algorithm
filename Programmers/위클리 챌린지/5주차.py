def solution(word):
    answer = 0
    flag = False
    
    def check(st):
        nonlocal answer
        nonlocal flag
        if st == word:
            print(st)
            flag = True
            return
        if len(st) >= 5:
            return
        for s in ['A','E','I','O','U']:
            answer+=1
            check(st+s)
            if flag:
                break
    
    check('')
            
    return answer
