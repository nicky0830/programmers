n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = []
s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(n):
        if arr[i] not in visited:
            if not s or arr[i] > s[-1]:
                s.append(arr[i])
                visited.append(arr[i])
                dfs()
                s.pop()
                visited.pop()

dfs()
