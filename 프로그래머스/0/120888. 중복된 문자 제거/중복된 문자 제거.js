function solution(my_string) {
    answer = ''
    for(let m of my_string) {
        if (!answer.includes(m)) {
            answer += m
        }
    }
    return answer
}