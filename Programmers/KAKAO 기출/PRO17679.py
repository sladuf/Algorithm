# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    while True:
        delete = set()

        # 사라질 블록 count
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 0 :
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    delete.update([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])

        if not delete:
            break

        # 블록 지우기
        for i,j in delete:
            board[i][j] = 0
        
        # 블록 내리기
        for j in range(n-1,-1,-1):
            for i in range(m-1,-1,-1):
                if board[i][j] == 0:
                    for k in range(i,-1,-1):
                        if board[k][j] == 0:
                            continue
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break
    
    for i in range(m):
        answer += board[i].count(0)

    return answer

# m=4
# n=5
# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# result = solution(m, n, board)
# print(result)