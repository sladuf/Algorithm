# 21.02.23 [좋은 수열]
import sys

def ch(cnt):
    #좋은 수열인지 확인하기
    for i in range(1,cnt//2+1):
        if res[cnt-i:cnt] == res[cnt-(2*i):cnt-i]:
            return False

    #좋은 수열인데 길이가 n인지 확인
    if cnt == n:
        for i in res:
            print(i, end='')
        return True

    #아직 길이가 n이 아니라면 1,2,3 추가
    for i in range(1,4):
        #연속된 숫자 X
        if res[-1] == i:
            continue

        #i를 넣어보고 좋은 수열이 아니면 pop
        res.append(i)
        if ch(cnt+1):
            return True
        res.pop()

n = int(sys.stdin.readline())
res = [1]
ch(1)