N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(y, x):
    global max_count
    max_count += 1
    arr[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 and ny < N and nx >= 0 and nx < N:
            if arr[ny][nx] == 1:
                dfs(ny, nx)

answer = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            global max_count
            max_count = 0
            dfs(y, x)
            answer.append(max_count)
print(len(answer))
answer.sort()
for a in answer:
    print(a)