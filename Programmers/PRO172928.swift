// https://school.programmers.co.kr/learn/courses/30/lessons/172928
// 공원 산책

import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    //park를 이차원 배열로 변환
    let metrix = park.map { Array($0).map{ String($0)} }
    let (h,w) = (metrix.count, metrix[0].count)
    var result = [0,0]
    for i in 0..<h {
        var flag = false
        for j in 0..<w {
            if metrix[i][j] == "S" {
                result = [i,j]
                flag = true
                break
            }
        }
        if flag {
            break
        }
    }
    
    for route in routes{
        let temp = route.components(separatedBy:" ")
        let (op, n) = (temp[0], Int(temp[1])!)
        
        let direct = direction(op)
        var (x,y) = (result[0], result[1])
        var flag = true
        for i in 1...n {
            x+=direct[0]
            y+=direct[1]
            if x<0 || x>=h || y<0 || y>=w { 
                flag = false 
                break
            }
            if metrix[x][y] == "X" {
                flag = false
                break
            }
        }
        if flag { result = [x,y] }
    }
    
    return result
}

func direction(_ op: String) -> [Int] {
    if op == "N" {
        return [-1,0]
    } else if op == "S" {
        return [1,0]
    } else if op == "E" {
        return [0,1]
    } else {
        return [0,-1]
    }
}