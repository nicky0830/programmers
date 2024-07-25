T =  int(input())

for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    if n > 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
    for j in range(2, n):
        arr[0][j] = max(arr[0][j] + arr[1][j-1], max(arr[0][j-2], arr[1][j-2])+arr[0][j])
        arr[1][j] = max(arr[1][j] + arr[0][j-1], max(arr[0][j-2], arr[1][j-2])+arr[1][j])
    print(max(arr[0][n-1], arr[1][n-1]))