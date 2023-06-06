import Foundation
// st로 돌아가기, now 현재 Index , 총 합

func solution(_ n: Int, _ arr : [[Int]]){
    
    var visited = Array(repeating: false, count: n)
    var result = -1
    
    func bf(_ st : Int , _ now: Int, _ cnt: Int, _ nodeCnt : Int){
        if (nodeCnt == n){
            if arr[now][st] != 0{
                if result == -1 {
                    result = cnt+arr[now][st]
                }
                else{
                    result = min(cnt+arr[now][st], result)
                }
            }
            return
        }
        
        for i in 0..<n{
            if visited[i] == false && arr[now][i] != 0 {
                visited[i] = true
                bf(st, i, cnt+arr[now][i], nodeCnt+1)
                visited[i] = false
                
            }
        }
    }
    
    for i in 0..<n {
        visited[i] = true
        bf(i, i, 0, 1)
        visited[i] = false
    }
    
    print(result)
}

let n = Int(readLine()!)!
var arr = [[Int]]()
for _ in 0..<n{
    let temp = readLine()!.split(separator: " ").compactMap{ Int(String($0)) }
    arr.append(temp)
}

solution(n, arr)