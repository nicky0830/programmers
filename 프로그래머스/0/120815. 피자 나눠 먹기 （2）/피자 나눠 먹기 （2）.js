function solution(n) {
    var answer = 0;
    function gcd(a,b) {
        if (a%b == 0) {
            return b
        } 
        return gcd(b, a%b)
    }
    return n*6/gcd(n,6)/6
}