// https://school.programmers.co.kr/learn/courses/30/lessons/132265
// 롤케이크 자르기

import Foundation

// 제일 왼쪽이 0개, 오른쪽 모두 차지하도록 갯수 저장
// 딕셔너리와 셋을 이용해 갯수 저장
// 제일 왼쪽에서 오른쪽으로 이동하며 하나씩 가지며 갯수 트래킹

func solution(_ topping:[Int]) -> Int {
    
    var dictA = [Int:Int]()
    var dictB = [Int:Int]()
    var cntA = Set<Int>()
    var cntB = Set<Int>()
    
    for tp in topping {
        if let b = dictB[tp] {
            dictB[tp] = b+1
        } else {
            dictB[tp] = 1
        }
        cntB.insert(tp)
    }
    
    var result = 0
    for tp in topping {
        if let a = dictA[tp] {
            dictA[tp] = a+1
        } else {
            dictA[tp] = 1
            cntA.insert(tp)
        }
        let b = dictB[tp]!
        if b-1 == 0 {
            dictB[tp] = nil
            cntB.remove(tp)
        } else {
            dictB[tp] = b-1
        }
        if cntA.count == cntB.count {
            result += 1
        }
    }
    
    return result
}