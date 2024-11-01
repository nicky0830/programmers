function solution(s) {
    const stack = []
    s.split(' ').forEach(a => { 
        if (a != 'Z') stack.push(Number(a))
        else stack.pop()
    })
    return stack.reduce((acc, cur) => acc + cur,0);
}