// 2023.06.10
// 드래곤 커브

import Foundation

func solution(_ n: Int, _ curve: [[Int]]){
    var matrix = Array(repeating: Array(repeating: false, count: 101), count: 101)
    
    for c in curve{
        let x = c[0]
        let y = c[1]
        let d = c[2]
        let g = c[3]
        matrix[y][x] = true
        let derection = dragonCurve(d, g)
        check(x,y,derection)
    }
    
    var result = 0
    for i in 0..<100{
        for j in 0..<100 {
            if matrix[i][j] && matrix[i][j+1] && matrix[i+1][j] && matrix[i+1][j+1]{
                result+=1
            }
        }
    }
    
    print(result)
    
    func dragonCurve(_ d: Int, _ g: Int) -> [Int] {
        var derection = [d]
        for _ in 0..<g{
            for i in derection.reversed(){
                if i == 3{
                    derection.append(0)
                }else{
                    derection.append(i+1)
                }
            }
        }
        
        return derection
    }
    
    func check(_ x: Int, _ y: Int, _ derection: [Int]){
        var a = y
        var b = x
        for i in derection{
            switch i{
            case 0:
                if b+1 <= 100 {
                    matrix[a][b+1] = true
                    b += 1
                }
            case 1:
                if 0 <= a-1 {
                    matrix[a-1][b] = true
                    a -= 1
                }
            case 2:
                if 0 <= b-1{
                    matrix[a][b-1] = true
                    b -= 1
                }
            case 3:
                if a+1 <= 100{
                    matrix[a+1][b] = true
                    a += 1
                }
            default:
                continue
            }
        }
    }
}


let n = Int(readLine()!)!
var curve = [[Int]]()
for _ in 0..<n{
    let temp = readLine()!.split(separator: " ").compactMap{ Int($0) }
    curve.append(temp)
}

solution(n, curve)
