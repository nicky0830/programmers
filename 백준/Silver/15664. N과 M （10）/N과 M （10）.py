n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []
visited = []

def dfs():
    check = 0
    if len(s) == m:
        print(*s)
    for i in range(n):
        if i not in visited and check != arr[i] and (not s or s[-1] <= arr[i]):
            visited.append(i)
            s.append(arr[i])
            check = arr[i]
            dfs()
            s.pop()
            visited.pop()

dfs()