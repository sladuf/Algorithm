# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = [1]*len(places)
    
    for temp in range(len(places)):
        flag = True
        spot = places[temp]
        for x in range(len(spot)):
            for y in range(len(spot[x])):
                if spot[x][y] != 'P':
                    continue
                if y+1<len(spot[x]):
                    if spot[x][y+1] == 'P':
                        flag = False
                        break
                    if spot[x][y+1] == 'O' and y+2<len(spot[x]) and spot[x][y+2] == 'P':
                        flag = False
                        break
                if x+1<len(spot):
                    if 0<=y-1 and spot[x+1][y-1]=='P':
                        if spot[x][y-1] == 'X' and spot[x+1][y] == 'X':
                            pass
                        else:
                            flag = False
                            break
                    if y+1<len(spot[x]) and spot[x+1][y+1] == 'P':
                        if spot[x][y+1] == 'X' and spot[x+1][y] == 'X':
                            pass
                        else:
                            flag = False
                            break
                    if spot[x+1][y] == 'P':
                        flag = False
                        break
                    if spot[x+1][y] == 'O' and x+2<len(spot) and spot[x+2][y] == 'P':
                        flag =False
                        break
                if flag == False:
                    break
            if flag == False:
                break
        if flag == False:
            answer[temp] = 0
        
    return answer
