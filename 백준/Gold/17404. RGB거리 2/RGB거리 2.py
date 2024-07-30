n = int(input())
MAX_NUM = 1000 * n
arr = [list(map(int, input().split())) for _ in range(n)]
ans = MAX_NUM

for i in range(3):
    dp = [[MAX_NUM, MAX_NUM, MAX_NUM] for _ in range(n)]
    dp[0][i] = arr[0][i]
    for j in range(1,n):
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = arr[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = arr[j][2] + min(dp[j-1][1], dp[j-1][0])
    
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
            # dp의 마지막에서 첫번째 rgb와 다른
print(ans)