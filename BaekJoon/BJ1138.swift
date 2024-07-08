// https://www.acmicpc.net/problem/1138
// 10*10

import Foundation

func solution(_ n: Int, _ arr: [Int]) -> [Int]{
    
    var result = Array(repeating: 0, count: n)
    
    for i in 0..<n {
        let id = i+1
        var cnt = 0
        for j in 0..<n {
            if result[j] == 0 {
                if cnt == arr[i] {
                    result[j] = id
                    break
                } else {
                    cnt+=1
                }
            }
        }
    }
    
    return result
}

let n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }

let result = solution(n, arr)
for i in result {
    print(i, terminator: " ")
}
