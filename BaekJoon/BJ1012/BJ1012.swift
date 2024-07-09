// https://www.acmicpc.net/problem/1012
// 유기농 배추

import Foundation

// queue없으니까 dfs로 해결하자..

func solution(m:Int, n:Int, k:Int, spot: [[Int]]) -> Int {
    
    var metrix = Array(repeating: Array(repeating: 0, count: m), count: n)
    var visited = Array(repeating: Array(repeating: false, count: m), count: n)
    
    for s in spot {
        let (x,y) = (s[1],s[0])
        metrix[x][y] = 1
    }
    
    let dx = [1,-1,0,0]
    let dy = [0,0,1,-1]
    var result = 0
    
    for s in spot {
        let (x,y) = (s[1], s[0])
        if visited[x][y] {
            continue
        }
        result += 1
        dfs(x: x, y: y)
    }
    
    func dfs(x: Int, y: Int) {
        if visited[x][y] { return }
        visited[x][y] = true
        for i in 0..<4 {
            let xx = dx[i]+x
            let yy = dy[i]+y
            if 0<=xx && xx<n && 0<=yy && yy<m && metrix[xx][yy] == 1 && !visited[xx][yy] {
                dfs(x: xx, y: yy)
            }
        }
    }
    
    return result
}

let T = Int(readLine()!)!
for _ in 0..<T{
    let mnk = readLine()!.split(separator: " ").map { Int($0)! }
    let (m,n,k) = (mnk[0], mnk[1], mnk[2])
    var spot = [[Int]]()
    for _ in 0..<k {
        let temp = readLine()!.split(separator: " ").map{ Int($0)! }
        spot.append(temp)
    }
    let result = solution(m: m, n: n, k: k, spot: spot)
    print(result)
}
