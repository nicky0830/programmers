import sys
from collections import deque
n = int(sys.stdin.readline().strip())
q = deque()
for _ in range(n):
    s = sys.stdin.readline().strip().split()
    if s[0] == 'push':
        q.append(s[1])
    if s[0] == 'pop':
        if not q:
            print(-1)
        else:
            p = q.popleft()
            print(p)
    if s[0] == 'size':
        print(len(q))
    if s[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    if s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
