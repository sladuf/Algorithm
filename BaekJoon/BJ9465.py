# 21.03.02 [스티커]
'''
선택한 스티커의 상,하,좌,우는 선택 X
예외부분 : 대각선 or 대각선 한칸 옆 중에 큰 값 선택!!
'''
import sys

t = int(sys.stdin.readline())

for case in range(t):
    n = int(sys.stdin.readline())
    table = []
    for i in range(2):
        table.append(list(map(int, sys.stdin.readline().split())))
    if n == 1:
        print(max(table[0][0],table[1][0]))
    else:
        res = [table[x] for x in range(2)]
        #처음 시작 : 대각선 에 있는 값+=
        #res[0][] : 아래에서 첫번째 스티커를 선택한 경우
        #res[1][] : 위에서 첫번 째 스티커를 선택한 경우
        res[0][1] = table[1][0]+table[0][1]
        res[1][1] = table[0][0]+table[1][1]
        for i in range(2,n):
            #세번 째 칸부터 진행
            #왼쪽 대각선 or 대각선 한칸 옆 중에 큰 값과 자기 자신을 더한다
            res[0][i] = max(res[1][i-1], res[1][i-2]) + table[0][i]
            res[1][i] = max(res[0][i-1], res[0][i-2]) + table[1][i]
            
        print(max(table[0][-1],table[1][-1]))
