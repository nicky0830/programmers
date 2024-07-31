n = int(input())
arr = [[0 for _ in range(n+1)] for _ in range(2)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    t,p = map(int, input().split())
    arr[0][i] = t
    arr[1][i] = p


for i in range(n+1):
    new_t = i + arr[0][i]
    if new_t <= n:
        dp[new_t] = max(dp[new_t], max(dp[:i+1]) + arr[1][i])
    # 비교를 위해 max
    # dp[new_t]에 더하는 게 아니라 dp[i]에 더하는 거

print(max(dp))