n = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = arr[0]

max_val, min_val = arr[0], arr[0]
for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]
    if dp[i-1] < min_val:
        min_val = dp[i-1]
    if max_val < dp[i]:
        max_val = dp[i]
    if max_val < dp[i] - min_val:
        max_val = dp[i] - min_val
print(max_val)



