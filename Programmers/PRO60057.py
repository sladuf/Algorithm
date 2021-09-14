def ch(s, i):
    res = ''
    now = s[:i]
    cnt = 1
    j = i
    while True:
        if j+i > len(s):
            if cnt == 1:
                res += now+s[j:]
            else:
                res+=str(cnt)+now+s[j:]
            break
        if now == s[j:j+i]:
            cnt+=1
        else:
            if cnt == 1:
                res+=now
            else:
                res+=str(cnt)+now
            now = s[j:j+i]
            cnt = 1
        j+=i
    return len(res)
    
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        answer = min(answer,ch(s, i))
    return answer
