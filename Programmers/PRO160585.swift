// https://school.programmers.co.kr/learn/courses/30/lessons/160585
// 혼자서 하는 틱택토

import Foundation

// 선공"O" 후공"X"
// O < X 또는 O > X+1 -> 안됨
// O > X 라면, X가 이기면 안됨
// O == X 라면, O가 이기면 안됨


func solution(_ board:[String]) -> Int {
    
    let newBoard = board.map { Array($0).map{ String($0) } }
    var oCnt = 0
    var xCnt = 0
    
    for i in 0..<3 {
        for j in 0..<3 {
            if newBoard[i][j] == "O" {
                oCnt+=1
            } else if newBoard[i][j] == "X" {
                xCnt+=1
            }
        }
    }
    
    func winCheck(_ who: String) -> Bool {
        //가로
        for i in 0..<3 {
            var temp = true
            for j in 0..<3 {
                if newBoard[i][j] != who {
                    temp = false
                    break
                }
            }
            if temp { return true }
        }
        //세로
        for i in 0..<3 {
            var temp = true
            for j in 0..<3 {
                if newBoard[j][i] != who {
                    temp = false
                    break
                }
            }
            if temp { return true }
        }
        //대각선
        if newBoard[0][0] == who && newBoard[1][1] == who && newBoard[2][2] == who {
            return true
        }
        if newBoard[0][2] == who && newBoard[1][1] == who && newBoard[2][0] == who {
            return true
        }
        
        return false
    }
    
    
    if oCnt < xCnt {
        return 0
    } else if oCnt > xCnt {
        if oCnt > xCnt+1 { return 0 }
        if winCheck("X") { return 0 }
    } else if oCnt == xCnt {
        if winCheck("O") { return 0 }
    }
    
    return 1
}