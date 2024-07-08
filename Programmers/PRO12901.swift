// https://school.programmers.co.kr/learn/courses/30/lessons/12901
// 2016년

// week = [금,토,일,월,화,수,목]
// month = [index달이 총 몇 일인지]
// b + month 0부터 a-1 까지 더한값을 7로 나눈 나머지를 week에 대입

func solution(_ a:Int, _ b:Int) -> String {
    let week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    let month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    
    var temp = b
    for i in 0...a-1 {
        temp += month[i]
    }
    
    return week[temp%7]
}