# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def timeToSec(t):
    a,b = t.split(":")
    return int(a)*60 + int(b)

def sumTime(time):
    if len(time)%2 == 1:
        time.append("23:59")
    
    result = 0

    for idx in range(0,len(time),2):
        a = timeToSec(time[idx])
        b = timeToSec(time[idx+1])
        result += (b-a)
    
    return result

    

def totalFee(fees, time):
    totalTime = sumTime(time)

    if totalTime > fees[0]:
        return fees[1] + math.ceil((totalTime-fees[0])/fees[2]) * fees[3]
    else:
        return fees[1]


def solution(fees, records):
    answer = []
    car = dict()
    
    for record in records:
        time, num, _ = record.split(" ")
        if num in car:
            car[num].append(time)
        else:
            car[num] = [time]  
            
    carNumber = list(car.keys())
    
    for num in sorted(carNumber):
        answer.append(totalFee(fees, car[num]))
    
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print((solution((fees), records)))