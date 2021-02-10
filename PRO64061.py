# 21.02.10 [크레인 인형뽑기 게임]
def solution(board, moves):
    answer = 0
    top =[]
    for i in range(len(board)):
        temp = 0
        for j in range(len(board)):
            if board[j][i] != 0:
                temp = j
                break
        top.append(temp)
    stack = []
    for move in moves:
        pop = top[move-1]
        if pop == len(board):
            continue
        if stack:
            if stack[-1] == board[pop][move-1]:
                stack.pop()
                answer+=2
            else:
                stack.append(board[pop][move-1])
        else:
            stack.append(board[pop][move-1])
        top[move-1]+=1
        
    return answer