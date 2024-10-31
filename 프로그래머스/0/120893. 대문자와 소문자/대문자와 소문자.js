function solution(my_string) {
    var answer = '';
    for (let m of my_string) {
        if (m.toUpperCase() === m) {
            answer += m.toLowerCase()
        } else {
            answer += m.toUpperCase()
        }
    }
    return answer;
}