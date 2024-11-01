function solution(emergency) {
    var answer = [];
    const original = [...emergency]
    emergency.sort((a,b) => b-a)
    for(const a of original) {
        answer.push(emergency.indexOf(a)+1)
    }
    return answer;
}