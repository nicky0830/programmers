import sys
T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().strip()
    stack = []
    answer = ''
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                answer = 'NO'
                break
    if len(stack) == 0 and not answer:
        answer = 'YES'
    else:
        answer = 'NO'
    print(answer)
        
