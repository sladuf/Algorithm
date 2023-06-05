import Foundation

let n = Int(readLine()!)!
let top = readLine()!.split(separator: " ").compactMap{ Int(String($0)) }

var stack = [Int]()

var index = Array(repeating: 0, count: n)

for i in 0..<n{
    while stack.count > 0 {
        let temp = stack[stack.count-1]
        if top[temp] > top[i]{
            index[i] = temp+1
            break
        }
        else{
            stack.removeLast()
        }
    }
    stack.append(i)
}

var result = index.map{ String($0) }.joined(separator: " ")
print(result)