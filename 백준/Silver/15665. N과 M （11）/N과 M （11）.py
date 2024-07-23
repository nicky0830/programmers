n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

def dfs():
    check = 0
    if len(s) == m:
        print(*s)
        return
    for i in range(n):
        if check != arr[i]:
            s.append(arr[i])
            check = arr[i]
            dfs()
            s.pop()

dfs()