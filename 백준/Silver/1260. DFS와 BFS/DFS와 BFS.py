from collections import deque
n,m,v = map(int, input().split(' '))
arr = [[] for _ in range(n+1)]
dfs_visited = [False for _ in range(n+1)]
bfs_visited = [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

arr = list(map(lambda x: sorted(x), arr))

dfs_list = []
bfs_list = []
def dfs(n):
    dfs_list.append(n)
    dfs_visited[n] = True
    for now in arr[n]:
        if not dfs_visited[now]:
            dfs(now)
dfs(v)

def bfs(n):
    queue = deque()
    queue.append(n)
    bfs_visited[n] = True
    while queue:
        now = queue.popleft()
        bfs_list.append(now)
        for x in arr[now]:
            if not bfs_visited[x]:
                queue.append(x)
                bfs_visited[x] = True

bfs(v)
print(' '.join(list(map(lambda x: str(x),dfs_list))))
print(' '.join(list(map(lambda x: str(x),bfs_list))))
