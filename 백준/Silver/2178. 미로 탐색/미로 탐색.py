from collections import deque
n, m = map(int, input().split( ))
graph = [list(map(int, input())) for _ in range(n)]

def BFS(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
        # 가능한 모든 경로의 값을 이전 단계에서 계산하고 할당한다
            nx = x + dx[i]
            ny = y + dy[i]  
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1   
    return graph[n-1][m-1]

answer = BFS(0,0)
print(answer)