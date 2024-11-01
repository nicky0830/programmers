function solution(s) {
    const dict = {}
    const check = [...s]
    const answer = []
    check.forEach(a => a in dict ? dict[a]+=1 : dict[a]=1)
    for(const key of Object.keys(dict)) {
        console.log(key)
        if (dict[key]==1){
            answer.push(key)
        }
    }
    
    return answer.sort().join('')
}