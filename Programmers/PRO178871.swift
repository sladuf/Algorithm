// https://school.programmers.co.kr/learn/courses/30/lessons/178871
// 달리기 경주

import Foundation

// ranks = 선수의 등수 배열
// member = 선수의 등수 딕셔너리
// 불려진 선수의 등수를 member로 통해 알아내고, ranks와 member에 등수 변경

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var ranks = players
    var members = [String: Int]()
    
    for rank in 0..<players.count {
        members[ranks[rank]] = rank
    }
    
    for calling in callings {
        let rank = members[calling]!
        let a = ranks[rank]
        let b = ranks[rank-1]
        ranks[rank] = b
        ranks[rank-1] = a
        members[b] = rank
        members[a] = rank-1
    }
    
    return ranks
}