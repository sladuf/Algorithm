// 2023.06.07
// 거짓말

func solution(_ n: Int, _ m: Int, _ know: [Int], _ party_people: [[Int]]){
    
    var result = m
    var knowSet = Set(know[1..<know.count])
    
    for _ in 0..<m{
        for party in party_people {
            let temp = Set(party[1..<party.count])
            for i in knowSet{
                if temp.contains(i){
                    knowSet = knowSet.union(temp)
                    break
                }
            }
        }
    }
    
    for party in party_people {
        for i in knowSet{
            if party[1..<party.count].contains(i){
                result -= 1
                break
            }
        }
    }
    
    print(result)
    
}

let temp = readLine()!.split(separator: " ").compactMap{ Int($0) }
let n = temp[0]
let m = temp[1]
let know = readLine()!.split(separator: " ").compactMap{ Int($0) }
var party_people = [[Int]]()
for _ in 0..<m{
    let people = readLine()!.split(separator: " ").compactMap{ Int($0) }
    party_people.append(people)
}

solution(n, m, know, party_people)
