function solution(numbers, direction) {
    var answer = [];
    if (direction === 'left') {
        answer = [...numbers.slice(1), numbers[0]]
    } else {
        answer = [numbers[numbers.length-1], ...numbers.slice(0,-1)]
    }
    return answer;
}