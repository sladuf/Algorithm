import Foundation

func solution(_ n : Int, _ serial: [String]){
    
    var s = [[String]]()
    for i in 0..<n{
        let temp = serial[i].compactMap{ Int(String($0)) }.reduce(0, +)
        s.append([serial[i], String(temp)])
    }
    
    let sort_serial = s.sorted(by: { ($0[0].count, Int($0[1])!, $0[0]) < ($1[0].count, Int($1[1])!, $1[0]) })
    
    for i in sort_serial{
        print(i[0])
    }
}

let n = Int(readLine()!)!
var serial = [String]()
for _ in 0..<n{
    serial.append(readLine()!)
}

solution(n, serial)