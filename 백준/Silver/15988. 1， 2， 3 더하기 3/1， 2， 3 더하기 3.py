import sys
num = int(sys.stdin.readline().strip())
dp = [1, 2, 4, 7] 
for _ in range(num):
    m = int(sys.stdin.readline().strip())
    for i in range(len(dp), m+1):
        dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)
    print(dp[m-1])
