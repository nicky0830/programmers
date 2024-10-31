function solution(numbers, direction) {
    var answer = [];
    if (direction === 'left') {
        numbers.push(numbers.shift())
    } else {
        numbers.unshift(numbers.pop())
    }
    return numbers;
}