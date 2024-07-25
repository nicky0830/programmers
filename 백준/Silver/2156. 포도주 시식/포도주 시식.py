N = int(input())
dp = [0 for _ in range(N)]
arr =[]

for i in range(N):
    n = int(input())
    arr.append(n)
    if i >= 3:
        dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
    else:
        if i == 0:
            dp[i] = arr[0]
        if i == 1:
            dp[i] = dp[0] + arr[1]
        if i == 2:
            dp[i] = max(arr[0]+arr[2], arr[1]+arr[2], arr[0]+arr[1])

print(dp[N-1])