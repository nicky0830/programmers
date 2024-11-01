function solution(n) {
    let f = 1
    let i = 1
    while(f * i <= n) f *= i++
    return i-1
}