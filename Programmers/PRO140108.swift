// https://school.programmers.co.kr/learn/courses/30/lessons/140108
// 문자열 나누기

import Foundation

func solution(_ s:String) -> Int {
    
    var result = 0
    
    var arr = Array(s).map { String($0) }
    var len = arr.count
    var front = arr[0]
    var (a,b) = (1,0)
    
    for idx in 1..<len {
        if a == b {
            result += 1
            front = arr[idx]
            (a,b) = (1,0)
        } else {
            if front == arr[idx] { a += 1 }
            else { b += 1}
        }
    }
    
    if a > 0 { result += 1 }
    
    return result
}