function solution(numbers) {
    var answer = 0;
    const check = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    for(let c of check) {
        numbers = numbers.replaceAll(c, check.indexOf(c))
    }
    console.log(numbers)
    return Number(numbers);
}