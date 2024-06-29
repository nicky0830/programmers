import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,  sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(n):
    visited[n] = True
    for x in arr[n]:
        if not visited[x]:
            dfs(x)

answer = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        answer +=1

print(answer)