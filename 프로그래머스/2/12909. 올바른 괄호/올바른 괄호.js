function solution(s){
    let answer = true;
    let i;
    let j = 0;
    let head = 0;
    for(i = 0; i < s.length; i++) {
        if(s[i] === "("){
            head++;
        } else {
            if(head === 0){
                return false;
            }else{
                head--;
            }
        }
    }

    if(head > 0){
        return false;
    }

    return answer;
}