# https://school.programmers.co.kr/learn/courses/30/lessons/92334

import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    //신고 한사람 담아두기  k:v k: 신고받은애, v: 신고한사람
    //연락받은 횟수 k:v k:신고한사람, v:count
    
    var list = [String: Set<String>]()
    var contect = [String: Int]()
    var result = [Int]()
    
    for str in report{
        let id = str.split(separator: " ").map{String($0)}
        let reporter = id[0]
        let reported = id[1]
        if list[reported] == nil {
            list[reported] = [reporter]
        }
        else{
            list[reported]!.insert(reporter)
        }
    }
    
    for (key,v) in list {
        if v.count >= k {
            for vv in list[key]! {
                if contect[vv] == nil{
                    contect[vv] = 1
                }
                else{
                    contect[vv]! += 1
                }
            }
        }
    }
    
    for id in id_list {
        if let counting = contect[id] {
            result.append(counting)
        }
        else{
            result.append(0)
        }
    }
    
    return result
}