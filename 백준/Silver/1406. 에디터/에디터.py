import sys
s1 = list(sys.stdin.readline().strip())
s2 = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'L':
        if s1:
            s2.append(s1.pop())
    if command[0] == 'D':
        if s2:
            s1.append(s2.pop())
    if command[0] == 'B':
        if s1:
            s1.pop()
    if command[0] == 'P':
        s1.append(command[1])

print(''.join(s1) + ''.join(reversed(s2)))