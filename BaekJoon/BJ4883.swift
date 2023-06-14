// 2023.06.14
// 삼각그래프


import Foundation

func solution(_ n : Int, _ arr : [[Int]]) -> Int {
    var visited = arr
    
    visited[0][2] = min(visited[0][1] + arr[0][2], visited[0][1])
    
    visited[1][0] += visited[0][1]
    visited[1][1] += min(visited[1][0], visited[0][1], visited[0][2])
    visited[1][2] += min(visited[1][1], visited[0][1], visited[0][2])

    
    for i in 2..<n {
        for j in 0..<3{
            switch j{
            case 0:
                visited[i][j] += min(visited[i-1][j], visited[i-1][j+1])
            case 1:
                visited[i][j] += min(visited[i][j-1], visited[i-1].min()!)
            case 2:
                visited[i][j] += min(visited[i][j-1], visited[i-1][j-1], visited[i-1][j])
            default:
                break
            }
        }
    }
    
    return visited[n-1][1]
}

var cnt = 1
while true{
    let n = Int(readLine()!)!
    if n == 0{
        exit(0)
    }
    else{
        var arr = [[Int]]()
        for _ in 0..<n{
            let temp = readLine()!.split(separator: " ").compactMap{ Int($0) }
            arr.append(temp)
        }
        print("\(cnt). \(solution(n, arr))")
    }
    cnt+=1
}
            
