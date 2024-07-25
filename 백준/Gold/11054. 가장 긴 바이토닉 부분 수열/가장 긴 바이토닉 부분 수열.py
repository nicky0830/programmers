n = int(input())
arr = list(map(int, input().split()))
max_dp = [1 for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            max_dp[i] = max(max_dp[i], max_dp[j]+1)

for i in range(1,n):
    for j in range(i):
        if arr[i] < arr[j]:
            max_dp[i] = max(max_dp[i], max_dp[j] + 1)


print(max(max_dp))
