N, K = map(int, input().split())
arr = [[1 for _ in range(N+1)] for _ in range(K+1)]
for i in range(1,K+1):
    for j in range(1,N+1):
        arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000000

print(arr[K-1][N])