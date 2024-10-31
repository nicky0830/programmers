function solution(my_string, n) {
    var answer = '';
    answer = [...my_string].map(m => m.repeat(n)).join('')
    return answer;
}