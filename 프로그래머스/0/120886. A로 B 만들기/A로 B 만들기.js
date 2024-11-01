function solution(before, after) {
    var answer = 1;
    const b = [...before].sort()
    const a = [...after].sort()
    console.log(a,b)
    for (let i in before) {
        if (b[i] !== a[i]) {
            answer = 0
        }
    }
    return answer;
}