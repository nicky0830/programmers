function solution(my_string) {
    var answer = '';
    for(let m of my_string) {
        if (!'aeiou'.includes(m)) {
            answer += m
        }
    }
    return answer;
}