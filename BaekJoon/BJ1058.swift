// https://www.acmicpc.net/problem/1058
// 친구

import Foundation

// 이차원 배열로 친구 수 등록
// 본인 친구의 친구를 친구로 추가
// 가장 친구 많은 배열 찾기

func solution(n: Int, friendship: [String]) -> Int {
    var result = 0
    var twoFriends = [Set<Int>]()
    
    for friend in friendship {
        let temp = Array(friend)
        var two = Set<Int>()
        for i in 0..<n {
            if temp[i] == "Y"{
                two.insert(i)
            }
        }
        twoFriends.append(two)
    }
    
    for i in 0..<n {
        var temp = twoFriends[i]
        for friend in twoFriends[i] {
            temp.formUnion(twoFriends[friend])
        }
        result = max(result, temp.count-1)
    }
    
    return result
}

let n = Int(readLine()!)!
var friendship = [String]()
for _ in 0..<n {
    let temp = readLine()!
    friendship.append(temp)
}
let result = solution(n: n, friendship: friendship)
print(result)
