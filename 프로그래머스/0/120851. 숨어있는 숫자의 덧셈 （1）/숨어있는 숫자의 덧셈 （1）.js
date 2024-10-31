function solution(my_string) {
    var answer = 0;
    for(let m of my_string){
        if (!isNaN(m)){
            answer += Number(m)
        }
    }
    return answer;
}