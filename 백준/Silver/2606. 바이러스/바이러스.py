C = int(input())
P = int(input())
arr = [[] for _ in range(C+1)]
visited = [False for _ in range(C+1)]
visited[0] = None

for _ in range(P):
    a,b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

def dfs(n):
    visited[n] = True
    for x in arr[n]:
        if not visited[x]:
            dfs(x)

dfs(1)
print(visited.count(True)-1)