// https://school.programmers.co.kr/learn/courses/30/lessons/161990
// 바탕화면 정리

import Foundation

func solution(_ wallpaper:[String]) -> [Int] {
    
    let screen = wallpaper.map { Array($0).map { String($0) } }
    
    let x = screen.count
    let y = screen[0].count
    var (lux,luy,rdx,rdy) = (x,y,0,0)
    
    for i in 0..<x {
        for j in 0..<y {
            if screen[i][j] == "#" {
                lux = min(lux,i)
                luy = min(luy,j)
                rdx = max(rdx,i+1)
                rdy = max(rdy,j+1)
            }
        }
    }
    
    return [lux,luy,rdx,rdy]
}