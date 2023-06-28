// 2023.06.28

import Foundation

// 날짜를 숫자로 변환 -> year*365 + month*28 + day
// 약관의 종류는 딕셔너리로 만들어서 유효기간을 month*28로 변환
// 반복문을 돌며 발급 날짜에 딕셔너리에 있는 유효기간 더하고, 오늘보다 크면 담아두기

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    var answer = [Int]()
    
    let now = toInt(today)
    var dic = [String: Int]()
    
    for term in terms{
        let tmp = term.split(separator: " ").map{ String($0) }
        dic[tmp[0]] = Int(tmp[1])!*28
    }
    for i in 0..<privacies.count{
        let tmp = privacies[i].split(separator: " ").map{ String($0) }
        let day = toInt(tmp[0])
        let kind = tmp[1]
        if dic[kind]!+day <= now {
            answer.append(i+1)
        }
    }
    
    return answer
}

func toInt(_ str : String)-> Int{
    let tmp = str.split(separator: ".").map { Int($0)! }
    return tmp[0]*28*12 + tmp[1]*28 + tmp[2]
}