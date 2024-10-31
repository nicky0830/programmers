function solution(my_string) {
    var answer = [];

    return  [...my_string].filter(m => !isNaN(m)).map(m => Number(m)).sort((a,b) => a-b);
}