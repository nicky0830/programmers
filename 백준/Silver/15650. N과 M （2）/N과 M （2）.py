n, m = map(int, input().split())

s = []
visited = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(1, n+1):
        if i not in visited:
            if not visited or visited[-1] < i:
                s.append(i)
                visited.append(i)
                dfs()
                visited.remove(i)
                s.pop()
dfs()