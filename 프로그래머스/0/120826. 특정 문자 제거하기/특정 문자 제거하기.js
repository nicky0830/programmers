function solution(my_string, letter) {
    return my_string.split('').filter(m => m != letter).join('');
}