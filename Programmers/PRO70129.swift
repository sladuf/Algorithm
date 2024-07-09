// https://school.programmers.co.kr/learn/courses/30/lessons/70129
// 이진 변환 반복하기

import Foundation

func solution(_ s:String) -> [Int] {
    
    var (cnt, zero) = (0,0)
    var x = s
    while x != "1" {
        let next = removeZero(x)
        zero += x.count - next.count
        x = binary(next)
        cnt += 1
    }
    
    return [cnt, zero]
}

func binary(_ num: String) -> String {
    return String(num.count, radix: 2)
}

func removeZero(_ num: String) -> String {
    return num.filter { $0 == "1" }
}