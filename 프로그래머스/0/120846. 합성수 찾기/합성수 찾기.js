function solution(n) {
    const dp = new Array(n+1).fill(1)
    for(let i=2; i<=n; i++) {
        if (dp[i]) {
            for (let j=2; i*j<=n; j++) {
                dp[i*j] = 0
            }
        }
    }
    return dp.filter(d => d === 0).length
}