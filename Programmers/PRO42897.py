# 21.02.10 [도둑질]
'''
꼭!!!다시보고 복습해보기
단순DP는 아닌거같고 그리디 + DP인듯
점화식을 끌어내는 연습을 해야겠당
'''
def solution(money):
    answer = 0
    dp1 = [0 for x in range(len(money))]
    dp2 = [0 for x in range(len(money))]
    #dp1 0번째 집 터는경우(마지막 집 털 기회X)
    #dp2 1번째 집 터는경우(마지막 집 털 기회O)
    dp1[0] = money[0]
    dp1[1] = dp1[0]
    dp2[1] = money[1]
    
    for i in range(2,len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
        
    #마지막 집 털건지 말건지 check
    dp2[-1] = max(dp2[-2], dp2[-3]+money[-1])
        
    answer = max(max(dp1),max(dp2))
    return answer