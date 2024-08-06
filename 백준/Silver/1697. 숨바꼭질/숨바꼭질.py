from collections import deque

n,k = map(int, input().split())
MAX = 10 ** 5
memory = [0] * (MAX+1)
# 미리 최대의 메모리를 정해놔서 메모리 초과가 일어나지 않는다

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(memory[x])
            exit()
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not memory[nx]:
                memory[nx] = memory[x] + 1
                # count+1랑 똑같은데 따로 메모리로 저장할 뿐
              
                q.append(nx)

bfs()