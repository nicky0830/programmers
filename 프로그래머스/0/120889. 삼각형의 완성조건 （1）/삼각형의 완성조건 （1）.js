function solution(sides) {
    var answer = 0;
    m = Math.max(...sides)
    i = sides.indexOf(m)
    sides.splice(i, 1)
    const [a,b] = sides
    return  a+b > m ? 1 : 2;
}