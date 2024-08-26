def solution(land):
    answer = 0
    dp = [[0 for _ in range(4)]for _ in range(len(land))]
    
    for i in range(len(land)):
        for j in range(4):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                arr = dp[i-1][:j] + dp[i-1][j+1:]
                dp[i][j] = land[i][j] + max(arr)
    return max(dp[-1])