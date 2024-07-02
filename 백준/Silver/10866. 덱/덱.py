import sys
n = int(sys.stdin.readline())
deque = []
for _ in range(n):
    x = sys.stdin.readline().strip().split(' ')
    if x[0] == 'push_front':
        deque.insert(0, x[1])
    if x[0] == 'push_back':
        deque.append(x[1])
    if x[0] == 'pop_front':
        if len(deque) > 0:
            d = deque.pop(0)
            print(d)
        else:
            print(-1)
    if x[0] == 'pop_back':
        if len(deque) > 0:
            d = deque.pop()
            print(d)
        else:
            print(-1)
    if x[0] == 'size':
        print(len(deque))
    if x[0] == 'empty':
        if len(deque) > 0:
            print(0)
        else:
            print(1)
    if x[0] == 'front':
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)
    if x[0] == 'back':
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)