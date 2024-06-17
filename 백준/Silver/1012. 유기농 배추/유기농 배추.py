import sys
sys.setrecursionlimit(10000) 

T = int(input())
answers = []
for i in range(T):
    M,N,K = map(int, input().split(' '))

    arr = [[0 for _ in range(M)]for _ in range(N)]  
    for i in range(K):
        col, row = map(int , input().split(' '))
        arr[row][col] = 1

    def dfs(row, col):
        if row < 0 or row >= N or col < 0 or col >= M:
            return False
        else:
            if arr[row][col] == 1:
                arr[row][col] = 0
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
                return True
            else:
                return False
    answer = 0
    for a in range(N):
        for b in range(M):
            if arr[a][b] == 1:
                if dfs(a,b) == True:
                    answer += 1
    answers.append(answer)
for a in answers:
    print(a)
