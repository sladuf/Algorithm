// https://school.programmers.co.kr/learn/courses/30/lessons/172927
// 광물 캐기

import Foundation

// 5개로 묶어서 다이아, 철, 돌 갯수 많은 순으로 정렬
// 다이아, 철, 돌 곡괭이 순서로 위 정렬을 하나씩 소거

func solution(_ picks:[Int], _ minerals:[String]) -> Int {
    
    // [다이아, 철, 돌] 갯수
    var bundles = [[Int]]()
    
    // picks가 minerals보다 작은 경우 반례 방지
    let limit = picks.reduce(0,+) * 5
    
    var cnt = 0
    var temp = [0,0,0]
    for i in 0..<min(limit, minerals.count) {
        let mineral = minerals[i]
        if mineral == "diamond" {
            temp[0] += 1
        } else if mineral == "iron" {
            temp[1] += 1
        } else {
            temp[2] += 1
        }
        
        cnt+=1
        
        if cnt == 5 {
            bundles.append(temp)
            cnt = 0
            temp = [0,0,0]
        }
    }
    
    if cnt > 0 {
        bundles.append(temp)
    }
    
    bundles.sort(by: {
        ($0[0], $0[1], $0[2]) > ($1[0], $1[1], $1[2])
    })
    
    var p = picks
    var result = 0
    for bun in bundles {
        if p[0] > 0 {
            p[0]-=1
            result += bun.reduce(0, +)
        } else if p[1] > 0 {
            p[1]-=1
            result += (bun[0]*5) + bun[1] + bun[2]
        } else if p[2] > 0 {
            p[2]-=1
            result += (bun[0]*25) + (bun[1]*5) + bun[2]
        } else {
            break
        }
    }
    
    return result
}