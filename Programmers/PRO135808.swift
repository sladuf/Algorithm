// https://school.programmers.co.kr/learn/courses/30/lessons/135808
// 과일 장수

import Foundation

// 최고 사과 순서로 정렬하여 팔기

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    let len = score.count
    if len < m {
        return 0
    }
    
    var result = 0
    
    let scoreSort = score.sorted(by: >)
    var idx = m-1
    while idx < len {
        result += scoreSort[idx]*m
        idx+=m
    }
    
    return result
}