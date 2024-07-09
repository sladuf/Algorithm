// https://school.programmers.co.kr/learn/courses/30/lessons/138476
// 귤 고르기

import Foundation

// 갯수를 딕셔너리로 저장
// 딕셔너리 value값을 배열로 만들어 오름차순 정렬하여 k가 될 때 까지 pop

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    
    var dict = [Int:Int]()
    
    for tan in tangerine {
        if let cnt = dict[tan] {
            dict[tan] = cnt+1
        } else {
            dict[tan] = 1
        }
    }
    
    var value = dict.values.sorted(by: < )
    var result = 0
    var total = 0
    while total < k {
        let temp = value.popLast()!
        total += temp
        result += 1
    }
    
    return result
}