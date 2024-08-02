T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for i,e in enumerate(arr):
        graph[i+1].append(e)
        graph[i+1].sort()

    visited = []
    def bfs(start):
        for node in graph[start]:
            if node not in visited:
                visited.append(node)
                bfs(node)
    
    count = 0
    for i in range(1,N+1):
        if i not in visited:
            visited.append(i)
            bfs(i)
            count +=1
    print(count)

