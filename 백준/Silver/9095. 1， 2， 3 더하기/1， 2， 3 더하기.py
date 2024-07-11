m = int(input())
for _ in range(m):
    n = int(input())
    arr = [0] * (n+1)
    for i in range(n+1):
        if i == 1:
            arr[i] = 1
        if i == 2:
            arr[i] = 2
        if i == 3:
            arr[i] = 4
        if i > 3:
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    print(arr[n])