# 21.02.09 [타겟 넘버]
def solution(numbers, target):
    answer = 0
    def func(index, now):
        nonlocal answer
        if index == len(numbers):
            if target == now:
                answer+=1
            return
        #더하는 경우로 재귀
        func(index+1,now + numbers[index])
        #빼는 경우로 재귀
        func(index+1,now - numbers[index])
    func(0,0)
    return answer