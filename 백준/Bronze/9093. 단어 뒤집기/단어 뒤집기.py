import sys
T = int(sys.stdin.readline())
for _ in range(T):
    arr = sys.stdin.readline().split()
    s = ' '.join(list(map(lambda x:x[::-1], arr)))
    print(s)
