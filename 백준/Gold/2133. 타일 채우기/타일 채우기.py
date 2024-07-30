n = int(input())

dp = [0]*(n+1)

if n % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * dp[2] + 2
        # 가로 +2일 때 3가지 경우 가능
        # n만의 고유한 2가지 경우 추가
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2
            # dp[j] : 2부터 i-4까지 (가로가 각각 4, 6, 8..일 때 2가지 경우가 가능하니까)
    print(dp[n])