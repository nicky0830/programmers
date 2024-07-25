N = int(input())
dp = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    if i == 0:
        dp[0] = row
    else:
        for j in range(i+1):
            if j == 0:
                dp[i].append(dp[i-1][0] + row[0])
            elif j == i:
                dp[i].append(dp[i-1][i-1] + row[i])
            else:
                dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + row[j])

print(max(dp[N-1]))