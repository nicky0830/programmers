function solution(n) {
    var answer = 0;
    for (let i=1; i <= Math.floor(n/2); i++) {
        answer += i*2
    }
    return answer;
}