function solution(s1, s2) {
    var answer = 0;
    for (let s of s1) {
        if (s2.includes(s)) {
            i = s2.indexOf(s)
            s2.splice(i,1)
            answer += 1
        }
    }
    return answer;
}