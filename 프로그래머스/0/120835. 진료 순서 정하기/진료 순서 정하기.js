function solution(emergency) {
    var answer = emergency.slice().sort((a,b) => b-a)
    return emergency.map(e => answer.indexOf(e) + 1);
}