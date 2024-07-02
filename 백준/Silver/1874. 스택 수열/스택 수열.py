import sys
n = int(sys.stdin.readline().strip())
stack = []
answer = []
number = 1
for _ in range(n):
    now = int(sys.stdin.readline().strip())
    for num in range(number, now+1):
        stack.append(num)
        answer.append('+')
        number += 1
    if stack[-1] == now:
        stack.pop()
        answer.append('-')
    else:
        answer = 'NO'
        break
if answer == 'NO':
    print(answer)
else:
    for a in answer:
        print(a)