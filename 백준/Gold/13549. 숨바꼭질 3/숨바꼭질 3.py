import sys
from collections import deque
input = sys.stdin.readline
 
a,b = map(int,input().split())
limit = 100001
time = [0]*limit
 
def bfs(x,y):
    q = deque()
    if x == 0 :
        # 0에서 출발할 떼 *2를 하면 0이니까 +1을 무조건 했다고 친다
        q.append(1)
    else :
        q.append(x)
    
    while q:
        x = q.popleft()
        if y == x :
            return time[x]
        
        for nx in (x-1,x+1,x*2):
            if 0 <= nx < limit and time[nx]==0:
                if nx == 2*x :
                    time[nx] = time[x]
                    q.appendleft(nx)
                    # 범위 내에 있고 탐색하지 않았을 때 2x를 먼저 탐색해야하니 큐에 맨 앞에 넣어준다.
                else : 
                    time[nx] = time[x] + 1
                    q.append(nx)
 
if a==0:
    if b==0:
        # 시간이 아예 안 지난 경우
        print(0)
    else:
        print(bfs(a,b)+1)
else :
    print(bfs(a,b))