function solution(array) {
    var answer = [Math.max(...array), array.indexOf(Math.max(...array))];
    return answer;
}