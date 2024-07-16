N = int(input())
dp = [[0,0] for _ in range(N+1)]
for i in range(1, N+1):
    if i == 1:
        dp[1][0] = 0
        dp[1][1] = 1
    elif i == 2:
        dp[2][0] = dp[1][1]
    else:
        dp[i][0] = sum(dp[i-1])
        dp[i][1] = dp[i-1][0]

print(sum(dp[N]))